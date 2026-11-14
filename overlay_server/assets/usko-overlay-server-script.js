// Зеркальное отображение сиро/ака, если камеру поставили со стороны судей. ?mirror=1
const overlayParams = new URLSearchParams(window.location.search);
const isMirrorOverlay = overlayParams.get("mirror") === "1";

if (isMirrorOverlay) {
  document.documentElement.classList.add("overlay-mirror");
}

function pad(n) { return n < 10 ? "0" + n : "" + n; }

//Преобразовывает текст штарафы в число
function penaltyLevelToDots(val) {
  const s = val == null ? "" : val;

  if (!s) return 0;

  // варианты/синонимы — на всякий случай
  if (s === "Keikoku") return 1;
  if (s === "Chui") return 2;
  if (s === "Hansoku") return 3;

  // если прилетит что-то неожиданное — кружки не рисуем
  return 0;
}

//Рисуем кружочки для штрафов
function setPenaltyDots(el, penaltyStr) {
  if (!el) return;

  const raw = penaltyStr == null ? "" : penaltyStr;
  // if (!raw) {
  //   el.innerHTML = "";
  //   return;
  // }

  const n = penaltyLevelToDots(raw);

  el.innerHTML = "";
  for (let i = 1; i <= 3; i++) {
    const d = document.createElement("span");
    d.className = "pen-dot" + (i <= n ? " filled" : "");
    el.appendChild(d);
  }
}


let state = null;
let ws = null;
let tatamiId = null; // lastTimerUpdate больше не нужен, удаляем
let lastOverlaySeq = 0;

// --- хелпер для глубокого merge ---
function deepMerge(target, source) {
  if (!source || typeof source !== "object") return target;

  Object.keys(source).forEach((key) => {
    const srcVal = source[key];
    const tgtVal = target ? target[key] : undefined;

    if (srcVal && typeof srcVal === "object" && !Array.isArray(srcVal)) {
      // вложенный объект: рекурсивно сливаем
      if (!tgtVal || typeof tgtVal !== "object" || Array.isArray(tgtVal)) {
        target[key] = {};
      }
      deepMerge(target[key], srcVal);
    } else {
      // примитивы и массивы — просто перезаписываем
      if (!target) return;
      target[key] = srcVal;
    }
  });

  return target;
}

function connect() {
  const loc = window.location;
  const parts = loc.pathname.split("/");
  tatamiId = parts[parts.length - 1] || "1";

  const proto = loc.protocol === "https:" ? "wss" : "ws";
  const wsUrl = proto + "://" + loc.host + "/ws/" + tatamiId;

  ws = new WebSocket(wsUrl);

  // ws.onopen = () => {
  //   console.log("WS connected");
  // };

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    const incomingSeq = Number(data.overlay_seq || 0);

    if (incomingSeq && incomingSeq < lastOverlaySeq) {
      return;
    }

    if (incomingSeq) {
      lastOverlaySeq = incomingSeq;
    }
    // Если это полный стейт (нет partial) — просто заменяем
    if (!data.partial) {
      state = data;
    } else {
      // Частичное обновление: аккуратно вольём в существующий state
      if (!state) {
        state = {};
      }
      deepMerge(state, data);
    }

    render();
  };
  ws.onclose = () => {
    console.log("WS disconnected, retrying...");
    setTimeout(connect, 2000);
  };
}

function isFinalFlagOn(value) {
  return value === true || value === 1 || value === "1" || value === "true";
}

function getKataScoreValues(scores, markDropped) {
  const vals = [];
  if (!scores) return vals;

  for (let i = 1; i <= 7; i++) {
    const key = "ref" + i;
    const raw = scores[key];
    if (raw == null) continue;

    const text = raw.toString().trim();
    if (!text || text === "0.0" || text === "0") continue;

    const num = Number(text.replace(",", "."));
    if (!Number.isFinite(num) || num === 0) continue;

    vals.push({
      key: key,
      referee: i,
      value: text,
      num: num,
      isDropped: false
    });
  }

  if (markDropped && vals.length >= 3) {
    const nums = vals.map((x) => x.num);
    const minValue = Math.min(...nums);
    const maxValue = Math.max(...nums);

    const minItem = vals.find((x) => x.num === minValue);

    const maxOrder = [2, 1, 3, 4, 5, 6, 7];
    const maxItem = maxOrder
      .map((referee) => vals.find((x) => x.referee === referee && x.num === maxValue))
      .find(Boolean);

    if (minItem) minItem.isDropped = true;
    if (maxItem) maxItem.isDropped = true;
  }

  return vals;
}

function renderKataScoreChips(el, vals, options) {
  if (!el) return;

  const opts = options || {};
  const chipClass = opts.chipClass || "kata-score-chip";
  const includeTotal = opts.includeTotal === true;
  const total = opts.total || "";

  el.innerHTML = "";

  vals.forEach((item) => {
    const chip = document.createElement("span");
    chip.className = chipClass + (item.isDropped ? " is-dropped" : "");
    chip.textContent = item.value;
    el.appendChild(chip);
  });

  if (includeTotal && total) {
    const totalChip = document.createElement("span");
    totalChip.className = chipClass + " is-total";
    totalChip.textContent = total;
    el.appendChild(totalChip);
  }

  el.style.display = vals.length > 0 || total ? "flex" : "none";
}

function render() {
  if (!state) return;

  const main = document.getElementById("overlay-main");
  const full = document.getElementById("overlay-winner");

  const fighters   = document.querySelector(".fighters");
  const penRow     = document.querySelector(".penalties-row");
  const timerEl    = document.getElementById("timer");
  const scoresEl   = document.getElementById("scores");
  const sumEl      = document.getElementById("sum");
  const catEl      = document.getElementById("category");
  const roundEl    = document.getElementById("round");
  const discEl     = document.getElementById("discipline");
  const tatamiEl   = document.getElementById("tatami");

  const totalRow = document.getElementById("final_total_row");
  const totalVal = document.getElementById("final_total_value");

  // ---------- РЕЖИМ МЕНЮ / IDLE ----------
  if (state.mode === "idle") {
    if (main) main.style.display = "block";
    if (full) full.style.display = "none";

    // Очищаем заголовки, оставляем только номер татами
    if (catEl)   catEl.textContent   = "";
    if (roundEl) roundEl.textContent = "";
    if (discEl)  discEl.textContent  = "";

    if (tatamiEl) {
      // ------ УПРАВЛЕНИЕ ОТОБРАЖЕНИЕМ "Татами" -------
      const tatamiEl = document.getElementById("tatami");

      // Условия скрытия:
      // - есть категория (state.category)
      // - или указана дисциплина
      // - или это ката/кумите режим
      const shouldHideTatami =
          (state.category && state.category.trim() !== "") ||
          (state.discipline && state.discipline.trim() !== "") ||
          (state.mode && state.mode !== "idle");

      // Если нужно скрыть — скрываем
      if (shouldHideTatami) {
          if (tatamiEl) tatamiEl.style.display = "none";
      } else {
          // Показываем в «пустом» состоянии
          if (tatamiEl) {
              tatamiEl.style.display = "block";

              // Если Python присылает tatami — используем его
              if (state.tatami) {
                  tatamiEl.textContent = state.tatami;
              } else {
                  tatamiEl.textContent = "Татами";
              }
          }
      }
    }

    if (fighters) fighters.style.display = "none";
    if (penRow)   penRow.style.display   = "none";
    if (timerEl)  timerEl.textContent    = "";
    if (scoresEl) scoresEl.textContent   = "";
    if (sumEl)    sumEl.textContent      = "";

    if (full) full.style.display = "none";
    return;
  }

  const aka  = state.aka  || {};
  const siro = state.siro || {};

  // ---------- FULLSCREEN РЕЗУЛЬТАТ КАТА ФИНАЛ ----------
  const isKataFinalResult = state.mode === "kata_final" && isFinalFlagOn(state.final);

  if (isKataFinalResult) {
    const winnerObj = aka;
    const vals = getKataScoreValues(state.scores, true);

    if (main) main.style.display = "none";
    if (full) {
      full.style.display = "flex";
      full.classList.remove("aka-side", "siro-side", "kata-result");
      full.classList.add("kata-result");

      const labelEl = full.querySelector(".winner-label");
      const nameEl = document.getElementById("winner_full_name");
      const regEl  = document.getElementById("winner_full_region");
      const logoEl = document.getElementById("winner_full_logo");

      if (labelEl) labelEl.textContent = "РЕЗУЛЬТАТ";
      if (nameEl) nameEl.textContent = winnerObj.name || "";
      if (regEl)  regEl.textContent  = winnerObj.region || "";

      if (logoEl) {
        const url = resolveRegionLogoUrl(winnerObj);
        if (url) {
          logoEl.innerHTML = '<img src="' + url + '" alt="">';
          logoEl.style.display = "block";
        } else {
          logoEl.innerHTML = "";
          logoEl.style.display = "none";
        }
      }

      const bottomEl     = document.getElementById("winner_bottom");
      const bigScoreEl   = document.getElementById("winner_score_big");
      const sidePanelEl  = document.getElementById("winner_sidepanel");
      const kataPanelEl  = document.getElementById("winner_kata_panel");
      const pensEl       = document.getElementById("winner_penalties");
      const kataSumEl    = document.getElementById("winner_kata_sum");
      const kataScoresEl = document.getElementById("winner_kata_scores");

      if (bottomEl)    bottomEl.style.display = "flex";
      if (bigScoreEl)  bigScoreEl.style.display = "none";
      if (sidePanelEl) sidePanelEl.style.display = "block";
      if (kataPanelEl) kataPanelEl.style.display = "block";
      if (pensEl)      pensEl.style.display = "none";
      if (kataSumEl)   kataSumEl.textContent = state.sum || "00.0";

      renderKataScoreChips(kataScoresEl, vals, {
        chipClass: "winner-kata-score-chip"
      });
    }

    return;
  }
    // ---------- ПОЛНОЭКРАННЫЙ ПОБЕДИТЕЛЬ ----------
  const winnerSide = state.winner_side || null;

  if (winnerSide === "aka" || winnerSide === "siro") {
    if (main) main.style.display = "none";
    if (full) {
      full.style.display = "flex";
      full.classList.remove("aka-side", "siro-side");
      full.classList.add(winnerSide === "aka" ? "aka-side" : "siro-side");

      const winnerObj = winnerSide === "aka" ? aka : siro;

      const nameEl = document.getElementById("winner_full_name");
      const regEl  = document.getElementById("winner_full_region");
      const logoEl = document.getElementById("winner_full_logo");

      if (nameEl) nameEl.textContent = winnerObj.name || "";
      if (regEl)  regEl.textContent  = winnerObj.region || "";

      // логотип региона
      if (logoEl) {
        const url = resolveRegionLogoUrl(winnerObj);
        if (url) {
          logoEl.innerHTML = '<img src="' + url + '" alt="">';
          logoEl.style.display = "block";
        } else {
          logoEl.innerHTML = "";
          logoEl.style.display = "none";
        }
      }

      const bottomEl     = document.getElementById("winner_bottom");
      const bigScoreEl   = document.getElementById("winner_score_big");
      const sidePanelEl  = document.getElementById("winner_sidepanel");
      const kataPanelEl  = document.getElementById("winner_kata_panel");
      const pensEl       = document.getElementById("winner_penalties");

      if (bottomEl)    bottomEl.style.display = "none";
      if (bigScoreEl)  bigScoreEl.style.display = "none";
      if (sidePanelEl) sidePanelEl.style.display = "none";
      if (kataPanelEl) kataPanelEl.style.display = "none";
      if (pensEl)      pensEl.style.display = "none";

      // --- KATA FINAL: большой блок суммы слева ---
      if (state.mode === "kata_final") {
        if (bigScoreEl) {
          bigScoreEl.textContent = (state.sum || "00.0");
          bigScoreEl.style.display = "flex";
        }
        // справа ничего не показываем
      }

      // --- KUMITE: большой счёт слева + штрафы справа ---
      if (state.mode === "kumite") {
        if (bottomEl) bottomEl.style.display = "flex";

        if (bigScoreEl) {
          bigScoreEl.textContent = (winnerObj.score != null ? winnerObj.score : "0");
          bigScoreEl.style.display = "flex";
        }

        if (sidePanelEl) sidePanelEl.style.display = "block";
        if (pensEl) pensEl.style.display = "flex";

        const p = winnerObj.penalties || {};
        const hm = p.hm || "";
        const j  = p.j  || "";

        const hmTextEl = document.getElementById("winner_pen_hm_text");
        const jTextEl  = document.getElementById("winner_pen_j_text");
        if (hmTextEl) hmTextEl.textContent = hm;
        if (jTextEl)  jTextEl.textContent  = j;

        setPenaltyDots(document.getElementById("winner_pen_hm_dots"), hm);
        setPenaltyDots(document.getElementById("winner_pen_j_dots"),  j);
      }


      // --- прочие режимы: без счёта/штрафов ---
      else {
        // ничего
      }
    }
    return;
  }

  // ---------- ОБЫЧНЫЙ РЕЖИМ ТАБЛО ----------
  if (main) main.style.display = "block";
  if (full) full.style.display = "none";
  if (full) full.classList.remove("aka-side", "siro-side", "kata-result");
  if (fighters) fighters.style.removeProperty("display");

  // Заголовки
  if (catEl)   catEl.textContent   = state.category || "";
  if (roundEl) roundEl.textContent = state.round    || "";

  if (tatamiEl) {
    // ------ УПРАВЛЕНИЕ ОТОБРАЖЕНИЕМ "Татами" -------
    const tatamiEl = document.getElementById("tatami");

    // Условия скрытия:
    // - есть категория (state.category)
    // - или указана дисциплина
    // - или это ката/кумите режим
    const shouldHideTatami =
        (state.category && state.category.trim() !== "") ||
        (state.discipline && state.discipline.trim() !== "") ||
        (state.mode && state.mode !== "idle");

    // Если нужно скрыть — скрываем
    if (shouldHideTatami) {
        if (tatamiEl) tatamiEl.style.display = "none";
    } else {
        // Показываем в «пустом» состоянии
        if (tatamiEl) {
            tatamiEl.style.display = "block";

            // Если Python присылает tatami — используем его
            if (state.tatami) {
                tatamiEl.textContent = state.tatami;
            } else {
                tatamiEl.textContent = "Татами";
            }
        }
    }
  }

  // Вид соревнований
  let discipline = "";
  if (state.discipline) {
    discipline = state.discipline;
  } else if (state.mode && state.mode.startsWith("kata")) {
    discipline = "КАТА";
  } else if (state.mode === "kumite") {
    discipline = "КУМИТЕ";
  }
  if (discEl) {
    discEl.textContent = discipline ? ("Вид: " + discipline) : "";
  }

  // Имена и счёт
  document.getElementById("aka_name").textContent  = aka.name  || "";
  document.getElementById("aka_score").textContent = (aka.score != null ? aka.score : "");
  document.getElementById("siro_name").textContent = siro.name || "";
  document.getElementById("siro_score").textContent = (siro.score != null ? siro.score : "");

  // Регионы под ФИО
  const akaRegEl = document.getElementById("aka_region");
  const siroRegEl = document.getElementById("siro_region");

  if (akaRegEl)  akaRegEl.textContent  = aka.region  || "";
  if (siroRegEl) siroRegEl.textContent = siro.region || "";

    // Флаги регионов (если присланы)
  const akaFlagEl  = document.getElementById("aka_flag");
  const siroFlagEl = document.getElementById("siro_flag");

  if (akaFlagEl) {
    const url = resolveRegionLogoUrl(aka);
    if (url) {
      akaFlagEl.innerHTML = '<img src="' + url + '" alt="">';
      akaFlagEl.style.display = "block";
    } else {
      akaFlagEl.innerHTML = "";
      akaFlagEl.style.display = "none";
    }
  }

  if (siroFlagEl) {
    const url = resolveRegionLogoUrl(siro);
    if (url) {
      siroFlagEl.innerHTML = '<img src="' + url + '" alt="">';
      siroFlagEl.style.display = "block";
    } else {
      siroFlagEl.innerHTML = "";
      siroFlagEl.style.display = "none";
    }
  }


  // ---------- СКРЫТИЕ СИРО В КАТА ФИНАЛ ----------
  const siroRow = document.getElementById("siro_row");

  if (state.mode === "kata_final") {
    // скрываем СИРО
    if (siroRow) siroRow.style.display = "none";

    // центрируем АКА (чтобы не прилипал к левому краю)
    const akaRow = document.getElementById("aka_row");
    if (akaRow) {
      // akaRow.style.flex = "1 1 100%";
      // akaRow.style.justifyContent = "center";
      akaRow.style.color = "#f1f2f6";
    }
  } else {
    // во всех остальных режимах показываем СИРО обратно
    if (siroRow) siroRow.style.display = "flex";

    const akaRow = document.getElementById("aka_row");
    if (akaRow) {
      // akaRow.style.flex = "1 1 40%";
      // akaRow.style.justifyContent = "flex-start";
      akaRow.style.color = "#ff6b6b";
    }
  }


  // ---------- ШТРАФЫ (только для кумите) ----------
  const akaPen  = aka.penalties  || {};
  const siroPen = siro.penalties || {};

  const akaPenHmEl  = document.getElementById("aka_pen_hm");
  const akaPenJEl   = document.getElementById("aka_pen_j");
  const siroPenHmEl = document.getElementById("siro_pen_hm");
  const siroPenJEl  = document.getElementById("siro_pen_j");

  if (akaPenHmEl)  akaPenHmEl.textContent  = akaPen.hm  || "";
  if (akaPenJEl)   akaPenJEl.textContent   = akaPen.j   || "";
  if (siroPenHmEl) siroPenHmEl.textContent = siroPen.hm || "";
  if (siroPenJEl)  siroPenJEl.textContent  = siroPen.j  || "";

  setPenaltyDots(document.getElementById("aka_pen_hm_dots"),  akaPen.hm);
  setPenaltyDots(document.getElementById("aka_pen_j_dots"),   akaPen.j);
  setPenaltyDots(document.getElementById("siro_pen_hm_dots"), siroPen.hm);
  setPenaltyDots(document.getElementById("siro_pen_j_dots"),  siroPen.j);

  if (penRow) {
    if (state.mode === "kumite") {
      const hasAnyPenalty =
        (akaPen.hm  && akaPen.hm.trim()  !== "") ||
        (akaPen.j   && akaPen.j.trim()   !== "") ||
        (siroPen.hm && siroPen.hm.trim() !== "") ||
        (siroPen.j  && siroPen.j.trim()  !== "");

      penRow.style.display = hasAnyPenalty ? "flex" : "none";
      penRow.style.display =  "flex" ;
    } else {
      penRow.style.display = "none";
    }
  }

  // ---------- КАТА ФИНАЛ: оценки и сумма ----------
  if (scoresEl) {
    scoresEl.innerHTML = "";
    scoresEl.style.display = "none";
  }
  if (sumEl) sumEl.textContent = "";

  if (totalRow) totalRow.style.display = "none";
  if (totalVal) totalVal.textContent = "00.0";

  if (state.mode === "kata_final" && state.scores) {
    const isFinal = isFinalFlagOn(state.final);
    const vals = getKataScoreValues(state.scores, isFinal);

    renderKataScoreChips(scoresEl, vals, {
      chipClass: "kata-score-chip",
      includeTotal: isFinal,
      total: state.sum || ""
    });
  }


  // ---------- Таймер ----------
  updateTimer();
}

// ===== Создаём путь для лого региона
function resolveRegionLogoUrl(obj) {
  if (!obj) return "";

  // новый вариант: имя файла в assets/regions
  const name = obj.region_logo_url;
  if (name && typeof name === "string" && name.trim() !== "") {
    return "/assets/regions/" + encodeURIComponent(name.trim());
  }

  return "";
}

function updateTimer() {
  const timerEl = document.getElementById("timer");

  if (!state || !state.timer) {
    timerEl.textContent = "";
    return;
  }

  const timer = state.timer;

  if (typeof timer.remaining_sec !== "number") {
    timerEl.textContent = "";
    return;
  }

  const total = Math.max(0, Math.round(timer.remaining_sec));
  const m = Math.floor(total / 60);
  const s = total % 60;

  timerEl.textContent = pad(m) + ":" + pad(s);
}

// setInterval(updateTimer, 200);
connect();

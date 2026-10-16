"""Ссылка и готовый QR скачивания: без сети и дополнительных библиотек при запуске."""

DOWNLOAD_URL = 'https://docs.google.com/spreadsheets/d/1Ea97ZKAnd4O9O6h3XgqHHd-35EBrWBFpqwM1yrj7UnQ/edit?gid=0#gid=0'

# QR содержит DOWNLOAD_URL, коррекция M, белое поле шириной 4 модуля.
# Встроенный PNG попадёт в EXE как часть Python-модуля, без внешнего файла.
# При смене адреса необходимо заново сгенерировать QR и проверить декодирование.
DOWNLOAD_QR_PNG = (
    "iVBORw0KGgoAAAANSUhEUgAAAMQAAADECAIAAABPxBk8AAAEs0lEQVR42u3dwY5bQQhEURzl/395ss3G0utA0XZ07nI09jx7SlAC"
    "mn79/PwUMMEvXwGICcQEYgKICcQEYgIxAcQEYgIxAcQEYgIxgZiAHr9PX/B6vcYf4u+Zqnfv/+53nrz23fucfsbT53z3nqfPfPr+"
    "if+LyARpDsQEnmkvp57m+Hfv/8Q/Pflb7167ORff8VhPvp9NTywyQZoDMYFnynqgTj3pyc87NaqOL5n6Wx0fM/V/EZkgzYGYwDN9"
    "Fqc+4/Tnm89fjb7kZg9OZAIxgZiA7/NMpzWPU88x9Qyn9ZvOPNPU5xKZIM2BmID7nunWDNBpnen0tYmZoc2Z7s3/i8gEYgIxgWeq"
    "tT5Rp6aSmIWa+nnn835L/05kAjGBmPAf8/q0Xk8n3yd6apv9sm/pwYlMICYQE3imip4F6/iV0/rKVA0m/fyJ/UxTz2A/E6Q5EBNQ"
    "/9ybO+1PdfLxlAfqzGtPzR519ixMfScdryYyQZoDMYFnqus7G2uxZ9eZQ0r0zhL7n6bqaiITpDkQEzDfm6uhHda3ZnrS9658Wi/v"
    "tC4lMkGaAzGh1JmueI4pb5Teqd2ZZ5rqkU15mqn3EZkgzYGYUOpMH3Uvx2Y/Lr3TaGquK7GDYMrLikyQ5kBMKHWm8dnhjofo7LSc"
    "8nan3mKzJrR5n53IBGkOxASeab5v9eS1m/sC0ufIOp6mM+/V+W5FJkhzICZg7+6UJ3l6ah586nx++p6W9N0mU3/LuTlIcyAmoMbP"
    "zW3uoqzwfstbezLTu0M357dEJkhzICaUOtN4P2vzvFj6LrzNfeiJep7IBGkOxATcv2+uk7M79+PemvXu/P7Ujob0Di2RCdIciAml"
    "zjSe46dmldIerrOXvOOlpp4hvQdLZII0B2JCqTNd2ZmUuDt283x+2ld9AupMkOZATEC2N5f2VVOebHMf1WaPLD2DLzJBmgMxgWfa"
    "63N9+31zm16qFutG5pkgzYGYgPu7BtL+afPOu2/0i3ZaQpoDMQGf5Zlu3d1xerYusbso8f7pO3rttIQ0B2IC7u8amNojcKses7k3"
    "8hNmp8yAQ5oDMQFZz7S573tq9ihR97o1h765P11kgjQHYkLZzxTNu6c+Jn0/Wnru+3TXeWKfeOcZRCZIcyAmIHtuLtELq8W78BJ3"
    "zNXiubbOLBfPBGkOxARUtM7U8RmJ2snpazufa+rMYGKH5+aeTJEJxARiQqkzXd9/vTn/tDk3PbUfIVEbM88EaQ7EBNQ/15kSfaJ0"
    "DebUQ0w9W8dXdbxmYoZdZII0B2JCqTN91gMNndWf8lK37pZJnz0se8AhzYGYgNqaZ6rw7PNpzu7Uk56c15vqoyXmjRKz4SITpDkQ"
    "EzDTm0uf80/MFW2eg5vyZ1O9vCffiToTpDkQEzDvmRJz3J3a0tRcdvr9p+o9Cd+pzgRpDsQEZD3TpveqD+sh3mLqLKE6E6Q5EBPw"
    "fZ4p7VcS59ESdwMn6knpHU4iE6Q5EBN4pjueZuoM/9+/f+pdEvWqzgzW1By6XQOQ5kBMwJ39TOlZ6amd1+n+2tSeyal74jb7iSIT"
    "iAnEhLKfCRCZQEwgJhATQEwgJhATQEwgJhATiAkgJhATiAkgJqT5A37jhJdHcYcXAAAAAElFTkSuQmCC"
)

#  SR MUZIK BOT telegramda sesli sohbet müzik botudur
## ✍🏻 Requirements

- FFmpeg
- Python 3.7+

## 🚀 Deployment

### 🛠 Configuration

1. Copy `example.env` to `.env` and fill it with your credentials.
2. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
3. Run:
   ```bash
   python -m callsmusic
   ```

### 🐬 Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ahnamerisetting/callsmusic)

## ℹ️ Commands

| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| /oynat  | yanıtlanan ses dosyasını veya YouTube videosunu oynat |
| /durdur | ses akışını duraklat |
| /devam  | ses akışını devam ettir |
| /ileri  | geçerli ses akışını atla |
| /sus    | userbot'u sessize al |
| /sesac  | userbot'un sesini aç |
| /bitir  | kuyruğu temizleyin ve userbot'u aramadan çıkarın |

## 📄 License

### GNU Affero General Public License v3.0-or-later

[Read more](http://www.gnu.org/licenses/#AGPL)

## ✨ Credits

- Il'ya ([tgcalls](https://github.com/MarshalX/tgcalls))
- Dan ([pyrogram](https://github.com/pyrogram/pyrogram))

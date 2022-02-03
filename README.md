# telegram-picoyplaca-bot

Documentación tomada de telegram-gustavo-bot
## Replit (se detiene)
- Ref: https://www.youtube.com/watch?v=NwBWW8cNCP4
- API_KEY Se configura como variable de ambiente en replit. Video lo hace crando archivo .env pero replit dice que eso está descontinuado

## Para Heroku (webhook y no pooling)
- Ref: https://www.youtube.com/watch?v=O0MAWtbg34g
- API_KEY agregada en Settings > Config Vars de Heroku
- https://www.youtube.com/watch?v=uKIxzYbqJtk
    - Indispensable decirle a telegram cual webhook debe llamar con el bot, para eso ir a URL:
    - https://api.telegram.org/botXXXXTOKENBOTXXXXX/setwebhook?url=XXXXXXURLHEROKUXXXX/XXXXTOKENBOTXXXX
    - Se tiene que agregar al final de la ruta el token porque "por buena practica de seguridad así se le está diciendo en el código"
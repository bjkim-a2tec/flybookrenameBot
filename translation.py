class Translation(object):
    START_TEXT = """반갑습니다,
전 도서관 리네임 봇입니다!

<b>이름을 변경할 파일에 답변을 하시고 Replay 부분에 /rm 새로운이름.확장자 를 넣어 주세요.</b>

자세한 것은 /help 명령어를 쳐보세요."""
    RENAME_403_ERR = "파일에 대한 권한이 없습니다."
    ABS_TEXT = " 깍쟁이가 되지 마세욤."
    UPGRADE_TEXT = "<b>👉 당신만의 복제 복을 만들어 보세요.. </b>  /help for Details"
    DOWNLOAD_START = "다운로드 중"
    UPLOAD_START = "업로드중"
    RCHD_TG_API_LIMIT = "{}초 안에 다운로드 됩니다.\n확인된 파일크기: {}\n죄송합니다. Telegram API 제한으로 인해 1.5GB보다 큰 파일을 업로드 할 수 없습니다."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**파일 이름 변경 완료!🤓.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{}초 안에 다운로드 됩니다.\n{}초안에 업로드 됩니다."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "확인된 파일크기: {}. 무료 사용자는 업로드 만 가능: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/el_profesor'>@el_profesor</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved. This image will be used in the File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "성공적으로 다운로드되었습니다."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "썸네일이 없습니다."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """안녕하세요. 리넴봇입니다..
    
1. Send me any Telegram File.
2. Reply to that message to /rm new name.extension.
   

--------

"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "파일의 답변을 달고 `/rm 변경될이름.확장자` 를 넣으세요."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """처리할 수 없습니다.
무료 사용자는 30 분마다 1 회만 요청 가능합니다.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """Telegram이 허용하는 파일 이름 제한은 {alimit} 자입니다.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@BuGGStreAM</code>
Please short your file name and try again!"""

from flask import Flask, render_template, Blueprint, redirect, url_for, request
from services import settings_service, telegram_service, whatsapp_service

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings", methods=["GET"])
def settings():
    return render_template('settings.html')



# -------------------------------------------------------------------------------------------------------------------------------------


# POST /settings/telegram
# save telegram details
@settings_bp.route("/settings/telegram", methods=['POST'])
def settings_telegram_save():
    bot_token = request.form["bot_token"]
    settings_service.save_telegram(bot_token)
    return redirect(url_for("settings.settings"))




# POST /settings/whatsapp
# save whatsapp details
@settings_bp.route("/settings/whatsapp", methods=['POST'])
def settings_whatsapp_save():
    phone_number_id = request.form["phone_number_id"]
    access_token = request.form["access_token"]
    settings_service.save_whatsapp(phone_number_id, access_token)
    return redirect(url_for("settings.settings"))



# POST /settings/messenger
# save messenger details
@settings_bp.route("/settings/messenger", methods=['POST'])
def settings_messenger_save():
    ig_user_id = request.form["ig_user_id"]
    access_token = request.form["access_token"]
    settings_service.save_whatsapp(ig_user_id, access_token)
    return redirect(url_for("settings.settings"))




# POST /settings/instagram
# save instagram details
@settings_bp.route("/settings/instagram", methods=['POST'])
def settings_instagram_save():
    page_id = request.form["page_id"]
    access_token = request.form["access_token"]
    settings_service.save_whatsapp(page_id, access_token)
    return redirect(url_for("settings.settings"))


# -----------------------------------------------------------------------------------------------------------------------------------



# POST /settings/telegram/test
# test telegram connection
@settings_bp.route("/settings/telegram/test", methods=['POST'])
def test_telegram():
    success = telegram_service.test_connection()
    if success:
        return {"status": "connected"}
    return {"status": "disconnected"}



# POST /settings/whatsapp/test
# test whatsapp connection
@settings_bp.route("/settings/telegram/test", methods=['POST'])
def test_whatsapp():
    success = whatsapp_service.test_connection()
    if success:
        return {"status": "connected"}
    return {"status": "disconnected"}



# POST /settings/messenger/test
# test messenger connection
@settings_bp.route("/settings/telegram/test", methods=['POST'])
def test_messenger():
    pass



# POST /settings/instagram/test
# test instagram connection
@settings_bp.route("/settings/telegram/test", methods=['POST'])
def test_instagram():
    pass

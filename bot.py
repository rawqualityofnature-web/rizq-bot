import os
import re
import json
import time
import random
import logging
from typing import Dict, Any

import requests
from flask import Flask, request, jsonify
from openai import OpenAI


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
META_VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "")
META_PAGE_ACCESS_TOKEN = os.getenv("META_PAGE_ACCESS_TOKEN", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini") 
BRAND_NAME = os.getenv("BRAND_NAME", "روو")

GRAPH_API_VERSION = "v23.0"
SEND_API_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}/me/messages"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


client = OpenAI(api_key=OPENAI_API_KEY)


conversation_history: Dict[str, list] = {}
customer_state: Dict[str, Dict[str, Any]] = {}
last_activity: Dict[str, Dict[str, float]] = {}


RISQ_SYSTEM_PROMPT = f"""
أنتِ رزق، من فريق المتجر.
أنتِ مساعدة خدمة عملاء ومبيعات لبراند {BRAND_NAME} الطبيعي للعناية بالشعر والبشرة والجسم.

الهوية:
- اسمك رزق.
- إذا سألت الزبونة: شنو اسمك؟ قولي: اسمي رزق 🤍
- إذا سألت: من وين؟ أو أي بلد؟ قولي فقط: أنا رزق، من فريق المتجر 🤍
- لا تذكري دولة معينة.
- إذا سألت الزبونة هل أنتِ AI؟ قولي بلطف: أنا مساعدة المتجر الافتراضية، وأقدر أحولك للفريق إذا حبيتي.

النبرة والأسلوب:
- الأساس لهجة سعودية ناعمة وراقية.
- إذا الزبونة كتبت عراقي، جاوبي بعراقي خفيف وراقي.
- إذا كتبت سوري/شامي، جاوبي بسوري/شامي خفيف وراقي.
- إذا اللهجة غير واضحة، استخدمي عربي ناعم ومفهوم.
- كوني دافئة، أنثوية، مهتمة، محترمة، قصيرة، وذكية بالإقناع.
- حسسي الزبونة إنك معها وتتابعينها بلطف، بدون مبالغة.
- لا تكرري نفس الجمل في الرسائل المتتالية.
- لا تكثري الإيموجيز: 1 إلى 2 فقط بالرسالة.
- كلمة “أبشري” تُستخدم أحياناً فقط، مو بكل رسالة، حتى تشعر الزبونة بالدلع والاهتمام.
- الترحيب الكامل يكون فقط في أول رسالة بالمحادثة:
  “هلا حبيبتي، أتمنى يومك جميل 🌸”
- بعد أول رسالة لا تعيدي التحية ولا تعيدي “أتمنى يومك جميل”.

طريقة الإقناع:
- لا تبيعي بشكل مباشر وفج.
- افهمي المشكلة أولاً، ثم اربطيها بالمنتج بطريقة ذكية.
- اسألي سؤال أو سؤالين كحد أقصى قبل التوصية.
- بعد إجابة الزبونة، اشرحي كيف المنتج مناسب لمشكلتها.
- دائماً أكدي المتابعة بعد الاستلام: نشرح الاستخدام ونتابع النتيجة.
- لا تقولي عبارات غير راقية مثل “نبيعك ونختفي”.

السلامة:
- لا تشخصي أمراض.
- لا تعدي بعلاج طبي مضمون.
- إذا ذكرت الزبونة حساسية شديدة، حمل، رضاعة، أدوية، مرض جلدي قوي، التهاب، جرح، أو أعراض مقلقة: ردي بلطف وارفعيها للفريق.

=========================
المنتج 1: بكج روو للشعر
=========================
الفوائد:
- مناسب للتساقط، الفراغات، ضعف البصيلات، التطويل، عدم نمو الشعر.
- مطوّر بنسبة ذهبية من المكونات الفعالة، خصوصاً إكليل الجبل.
- غني بالفيتامينات النباتية التي تساعد على إحياء البصيلات وتنشيطها.
- يدعم نمو خصلات شعر جديدة ويخفف الفراغات بشكل واضح.
- غالباً خلال أول أسبوعين يبدأ يبان تحسن ملحوظ مع الاستخدام المنتظم.
- ممتاز من أول استخدام للنعومة واللمعان.
- بعد شرح النتيجة قولي دائماً تقريباً:
  “وأنا راح أتابع استفادتك خطوة بخطوة لحد ما توصّلين للنتيجة اللي ترضيك 🌸”

الأسعار:
- العراق: 32 ألف دينار عراقي.
- سوريا: 220 ألف.

الشحن:
- العراق: بغداد 3 آلاف، المحافظات 5 آلاف.
- سوريا: دمشق مجاني، المحافظات 20 ألف.

الخصم:
- سوريا: إذا طلبت خصم، ممكن ينزل من 220 ألف إلى 200 ألف كبداية.
- العراق: إذا طلبت خصم على بكج الشعر، خصم حوالي 30 ألف حسب سياسة الإدارة.

طريقة الاستخدام الرسمية لبكج الشعر:
البكج يحتوي على سيرومين:
• السيروم الأول المكتوب عليه Scalp Mask يوضع على فروة الرأس ويوزّع بشكل جيد، ثم يُعمل مساج لمدة 5–10 دقائق لتنشيط البصيلات ✨
• السيروم الثاني الخاص بالوسط والأطراف يوضع على وسط وأطراف الشعر لتحسين الترطيب والمظهر الصحي 🌿
يُترك المنتج لمدة ساعتين ثم يُغسل، وإذا كان التساقط شديد ممكن يترك لليلة كاملة وبعدها يُغسل 👌
وتتكرر العملية من مرتين إلى 3 مرات بالأسبوع للحصول على أفضل نتيجة 🤍

=========================
المنتج 2: مقشر روو للجسم
=========================
الوصف:
- مقشر جسم فيزيائي مصنوع من الحرير وألواح الشجر.
- يخلّص الجسم من 99% من الجلد الميت والأوساخ، وتظهر على شكل كتل أثناء الاستخدام.
- فيزيائي مو كيميائي.
- آمن للكل حتى الحامل.
- يوجد منه أنواع حسب بشرة الجسم: حساسة، جافة، عادية، مختلطة/دهنية.

قبل تثبيت طلب المقشر:
- اسألي عن نوع بشرة الجسم حتى ينشحن لها النوع المناسب: حساسة، جافة، عادية، أو مختلطة.
- لا تطلبي الاسم والرقم فوراً بعد تحديد نوع البشرة.
- أولاً قولي مثلاً: “أبشري، متوفر النوع المناسب للبشرة العادية 🌸 إذا حابة أرتب لك الطلب ✨”
- إذا قالت نعم، بعدها اطلبي: الاسم + رقم الهاتف + العنوان بالتفصيل.

سؤال التشخيص المفضل:
“هدفك تنظيف عميق للجسم، تفتيح، أو علاج جلد الوزّة؟”

رد جلد الوزّة:
- قولي إنه ممتاز وسريع لعلاج جلد الوزّة.
- أغلب زبائننا شافوا فرق من أول أسبوعين.
- أكدي المتابعة: “وأنا راح أتابع حالتك”.

رد التنظيف العميق:
- أكدي أنه يخلص الجسم من 99% من الجلد الميت والأوساخ، وتظهر على شكل كتل أثناء الاستخدام.
- بعد الاستخدام تحس بنعومة واضحة وإحساس نظافة مريح.

رد التفتيح:
- اربطي التفتيح بإزالة الجلد الميت والتراكمات التي تسبب البهتان.
- مع الاستمرار يساعد على صفاء وتوحيد اللون.

الأسعار:
- العراق: 16 ألف للقطعة.
- سوريا: 110 ألف.

الشحن:
- العراق: بغداد 3 آلاف، المحافظات 5 آلاف.
- سوريا: دمشق مجاني، المحافظات 20 ألف.

خصم المقشر في العراق:
- الخصم فقط للكميات 10 قطع وفوق.
- الخصم 2 ألف للقطعة، من 16 ألف إلى 14 ألف للقطعة.
- لا تعطي خصم على قطعتين.

طريقة استخدام مقشر روو الرسمية، اكتبها كما يلي عند السؤال:
طريقة استخدام مقشر روو 🤍
أول شي نبلل الجسم لمدة 10 دقائق تحت ماء دافئ بخاري ، بدون استخدام أي صابون أو شامبو ✨
بعدها نبلل المقشر شوي بالماء الدافئ ونغلق الدش، وبعدها على طول الذراع  نبدأ الفرك بحركة من فوق لتحت وبضغط متوسط على نفس المنطقة ننكرر الحركة تقريباً 10–15 مرة لحد ما يبدأ الجلد الميت يطلع على شكل كتل رمادية 🌿
وتتكرر العملية على كامل الجسم ما عدا الوجه 👌
ويُستخدم كل 10–14 يوم

• المنتج استخدام شخصي فقط وممنوع مشاركته مع أفراد العائلة
• يُفضّل تغييره كل 3–6 أشهر
• يُحفظ بعيد عن الصابون أو الشامبو لأنهم يخربون فعالية المنتج 🤍

رسالة الليزر بعد طريقة استخدام المقشر:
وإذا تسوين جلسات ليزر، يُفضّل تستخدمين المقشر بعد 10 أيام من الجلسة حصراً ✨
لأنه يساعد على نتائج ليزر أنظف وأفضل 🌸
وما يُستخدم قبل 10 أيام من الليزر حتى نتجنب أي تحسس للبشرة 🤍

رسالة بعد الاستخدام للمقشر:
رأيك كثير يهمنا 🤍
وتسعديني إذا شاركتيني رأيك وتجربتك مع المنتج بعد الاستخدام 🌸

=========================
الطلبات والشكاوى والجملة والخروج
=========================
عند موافقة الزبونة على الطلب اطلبي تفاصيلها. صيغة التثبيت النهائية: "تمام 🤍 تم تثبيت طلبك، شكراً لاختيارك روو 🌸".
في الشكاوى لخصيها وفعّلي التنبيهات. في الجملة اطلبي رقم التواصل وفعّلي lead_type="wholesale".

مهم جداً: يجب أن يكون الرد دائماً بصيغة JSON صالحة ومطابقة للهيكل التالي تماماً:
{{
  "reply": "نص الرد المناسب للزبونة بناءً على التعليمات أعلاه",
  "dialect": "saudi|iraqi|syrian|neutral",
  "intent": "price|product_info|diagnosis|order|shipping|usage|complaint|cancel|discount|wholesale|followup|identity|unknown",
  "order_ready": false,
  "needs_owner_alert": false,
  "lead_type": "order|complaint|wholesale|none",
  "order": {{
    "customer_name": "",
    "phone": "",
    "country": "",
    "city": "",
    "address": "",
    "product": "",
    "quantity": "",
    "total": "",
    "notes": ""
  }}
}}
"""


def now_ts() -> float:
    return time.time()


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def get_history(user_id: str) -> list:
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    return conversation_history[user_id]


def is_first_message(user_id: str) -> bool:
    return user_id not in last_activity


def calculate_delay(user_id: str) -> float:
    current = now_ts()
    if user_id not in last_activity:
        return random.uniform(12, 15)

    last_customer = last_activity[user_id].get("last_customer_message", current)
    gap = current - last_customer

    if gap <= 120:
        return random.uniform(3, 4.5)
    if gap <= 1800:
        return random.uniform(10, 20)
    if gap <= 10800:
        return random.uniform(20, 40)
    return random.uniform(30, 60)


def parse_model_json(raw: str) -> Dict[str, Any]:
    try:
        return json.loads(raw)
    except Exception as e:
        logging.error(f"JSON Parse Error. Raw Data: {raw}. Hata: {e}")
        return {
            "reply": "تمام حبيبتي، ممكن توضّحين لي أكثر عشان أساعدك بالطريقة الأنسب؟ 🤍",
            "dialect": "neutral",
            "intent": "unknown",
            "order_ready": False,
            "needs_owner_alert": False,
            "lead_type": "none",
            "order": {
                "customer_name": "", "phone": "", "country": "", "city": "",
                "address": "", "product": "", "quantity": "", "total": "", "notes": ""
            }
        }


def build_input_messages(user_id: str, customer_text: str) -> list:
    history = get_history(user_id)
    state = customer_state.get(user_id, {})
    context = {
        "is_first_message_in_conversation": is_first_message(user_id),
        "known_customer_state": state,
        "runtime_rules": [
            "Do not repeat the full greeting except first message.",
            "Use only 1-2 emojis.",
            "Use 'أبشري' sometimes, not every message.",
            "Ask max 1-2 questions.",
            "Before scrub order, ask body skin type.",
            "If customer gives complete order info, set order_ready=true.",
            "If complaint or delivery delay, set needs_owner_alert=true."
        ]
    }

    messages = [
        {"role": "system", "content": RISQ_SYSTEM_PROMPT},
        {"role": "system", "content": json.dumps(context, ensure_ascii=False)},
    ]
    messages.extend(history[-16:])
    messages.append({"role": "user", "content": customer_text})
    return messages


def generate_risq_reply(user_id: str, customer_text: str) -> Dict[str, Any]:
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=build_input_messages(user_id, customer_text),
            temperature=0.75,
            response_format={"type": "json_object"} 
        )
        
        raw_output = response.choices[0].message.content.strip()
        data = parse_model_json(raw_output)
    except Exception as api_error:
        logging.error(f"OpenAI API Çağrı Hatası: {api_error}")
        data = parse_model_json("{}") 

    reply = data.get("reply", "").strip()

    history = get_history(user_id)
    history.append({"role": "user", "content": customer_text})
    history.append({"role": "assistant", "content": reply})

    state = customer_state.get(user_id, {})
    order = data.get("order", {}) or {}
    for key, value in order.items():
        if value:
            state[key] = value
    state["last_intent"] = data.get("intent", "unknown")
    state["last_dialect"] = data.get("dialect", "neutral")
    customer_state[user_id] = state

    return data



def send_instagram_message(recipient_id: str, text: str) -> Dict[str, Any]:
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    params = {"access_token": META_PAGE_ACCESS_TOKEN}
    try:
        response = requests.post(SEND_API_URL, params=params, json=payload, timeout=20)
        result = response.json() if response.text else {"status_code": response.status_code}
        if response.status_code >= 300:
            logging.error(f"Meta API Mesaj Gönderim Hatası: {result}")
        return result
    except Exception as e:
        logging.error(f"Meta API Bağlantı Hatası: {e}")
        return {"error": str(e)}


def extract_instagram_events(payload: Dict[str, Any]) -> list:
    events = []
    if not payload or "entry" not in payload:
        return events
        
    for entry in payload.get("entry", []):
        for item in entry.get("messaging", []):
            sender_id = item.get("sender", {}).get("id")
            message = item.get("message", {})
            text = message.get("text")

            if sender_id and text and not message.get("is_echo"):
                events.append({"sender_id": sender_id, "text": clean_text(text)})
    return events



def log_to_google_sheet(user_id: str, data: Dict[str, Any]) -> None:
    logging.info(f"GOOGLE SHEET LOG - User: {user_id} - Data: {json.dumps(data, ensure_ascii=False)}")


def send_owner_whatsapp_alert(alert_type: str, user_id: str, data: Dict[str, Any]) -> None:
    logging.warning(f"WHATSAPP ALERT - Type: {alert_type} - User: {user_id} - Data: {json.dumps(data, ensure_ascii=False)}")


def handle_side_effects(user_id: str, data: Dict[str, Any]) -> None:
    if data.get("order_ready"):
        log_to_google_sheet(user_id, {"type": "order", **data})
        send_owner_whatsapp_alert("new_order", user_id, data)

    if data.get("needs_owner_alert"):
        log_to_google_sheet(user_id, {"type": "urgent_complaint", **data})
        send_owner_whatsapp_alert("urgent_complaint", user_id, data)

    if data.get("lead_type") == "wholesale":
        log_to_google_sheet(user_id, {"type": "wholesale", **data})
        send_owner_whatsapp_alert("wholesale_lead", user_id, data)



@app.route("/", methods=["GET"])
def home():
    return "Risq Bot is online and optimized.", 200


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == META_VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    payload = request.get_json(force=True, silent=True) or {}
    logging.info(f"Gelen Webhook Verisi: {json.dumps(payload, ensure_ascii=False)}")

    events = extract_instagram_events(payload)

    for event in events:
        sender_id = event["sender_id"]
        text = event["text"]

        previous = last_activity.get(sender_id, {})
        last_activity[sender_id] = {
            **previous,
            "last_customer_message": now_ts(),
        }

        time.sleep(random.uniform(1.0, 2.0))

        data = generate_risq_reply(sender_id, text)
        reply_text = data.get("reply", "")

        delay = calculate_delay(sender_id)
        logging.info(f"Kullanıcı {sender_id} için {delay:.2f} saniye yanıt geciktiriliyor.")
        time.sleep(delay)

        if reply_text:
            send_instagram_message(sender_id, reply_text)
            last_activity[sender_id]["last_assistant_message"] = now_ts()

        handle_side_effects(sender_id, data)

    return jsonify({"status": "ok"}), 200


@app.route("/test", methods=["POST"])
def local_test():
    body = request.get_json(force=True, silent=True) or {}
    user_id = body.get("user_id", "test_customer")
    text = clean_text(body.get("text", ""))

    if not text:
        return jsonify({"error": "text field is required"}), 400

    previous = last_activity.get(user_id, {})
    last_activity[user_id] = {**previous, "last_customer_message": now_ts()}

    data = generate_risq_reply(user_id, text)
    return jsonify(data), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)

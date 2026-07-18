import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random

TOKEN = "8914972467:AAFyPTUs8v9JkAWsRTs4-ulcH_MQ9oKt-y0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚀 Get Signals", callback_data="start_signal")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🟢 <b>ELITESIGNAL PRO</b>\n\n"
        "Real-time Binary Options Signals\n"
        "Optimized for <b>Quotex</b>\n\n"
        "Tap below to start",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start_signal":
        keyboard = []
        pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "GBPJPY", "EURJPY", "USDCAD"]
        for pair in pairs:
            keyboard.append([InlineKeyboardButton(pair, callback_data=f"pair_{pair}")])
        
        await query.edit_message_text("Select Pair:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data.startswith("pair_"):
        pair = query.data[5:]
        direction = random.choice(["CALL 🟢", "PUT 🔴"])
        confidence = random.randint(78, 94)
        
        text = f"""
🟢 <b>ELITESIGNAL PRO</b> • LIVE

<b>Broker:</b> Quotex
<b>Pair:</b> {pair}
<b>Timeframe:</b> 5 Minutes

SIGNAL → <b>{direction}</b>
Confidence: <b>{confidence}%</b>

Trend: Strong
Momentum: Good
Volatility: Low

⏰ Expires in ~4:55
        """.strip()
        
        await query.edit_message_text(text, parse_mode='HTML')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("🚀 EliteSignal Pro is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

package main
import (
	"io/ioutil"
	"log"
  "strings"
	"github.com/go-telegram-bot-api/telegram-bot-api"
)
const CHANNEL_NAME = "@system_logs"
const FILE_PATH = "key.txt"
const QUESTION = `
<b>Challenge</b>
<i>Be the first one to answer this!</i>
#phys
Find the required current in A.
`
const INSTRUCTION = "Type your answer using the command <code>/ans [your answer with unit]</code> in any group with @kaito_bot or dm her. GOGOGO!"

const ANSWER = "4.8A"
const REPLY_TEXT = `
Answer(also source): <a href="https://youtu.be/CL34g5J8A3g">Check here!</a>
Stealing champion: `
const COMMAND = "/ANS "
const IMAGE_PATH = "image.png"

var inlineButton = tgbotapi.NewInlineKeyboardMarkup(
	tgbotapi.NewInlineKeyboardRow(
		tgbotapi.NewInlineKeyboardButtonURL("Give it a try","https://t.me/kaito_bot"),
	),
)

func getKey(path string) string {
		key, err := ioutil.ReadFile(path)
		if err != nil {
			log.Panicf("failed reading data from file: %s", err)
		}
		return string(key)
}

func main() {
	bot, err := tgbotapi.NewBotAPI(getKey(FILE_PATH))
	if err != nil {
		log.Panic(err)
	}
	//bot.Debug = true
	log.Printf("Authorized on account @%s", bot.Self.UserName)
	channelid := int64(-1001321795482);

	photo := tgbotapi.NewPhotoUpload(channelid, IMAGE_PATH)
  photo.Caption = QUESTION + INSTRUCTION
  log.Printf("1")
  photo.ParseMode = tgbotapi.ModeHTML
	photo.ReplyMarkup = inlineButton
  log.Printf("DOne")
  message, err := bot.Send(photo)
  log.Printf("Sent")

  u := tgbotapi.NewUpdate(0)
	u.Timeout = 60
	updates, err := bot.GetUpdatesChan(u)

  for update := range updates {
    if update.Message == nil { // ignore any non-Message Updates
			continue
		}

    log.Printf("[%s] %s: %s", update.Message.From.UserName, update.Message.From.FirstName + update.Message.From.LastName, update.Message.Text)

    if (strings.ToUpper(update.Message.Text) == (COMMAND + ANSWER)) {
      text := QUESTION + REPLY_TEXT + update.Message.From.FirstName + update.Message.From.LastName
      msg := tgbotapi.NewEditMessageText(message.Chat.ID, message.MessageID, text)
      msg.ParseMode = tgbotapi.ModeHTML
      msg.DisableWebPagePreview = true
      bot.Send(msg)

      msgReply := tgbotapi.NewMessage(update.Message.Chat.ID, "That's correct. Don't steal too much u bitch.")
      msgReply.ReplyToMessageID = update.Message.MessageID
      bot.Send(msgReply)
      break

	  } else if strings.Contains(strings.ToUpper(update.Message.Text), COMMAND) {
	    msgReply := tgbotapi.NewMessage(update.Message.Chat.ID, "WRong dude")
	    msgReply.ReplyToMessageID = update.Message.MessageID
	    bot.Send(msgReply)
	  }
}
  log.Printf("Program end.")
}

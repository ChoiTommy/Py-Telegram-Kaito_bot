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
<b>REVISION QUIZ</b>
<i>Be the first one to answer this!</i>
#chem #industrial_chem #catalyst
What is the catalyst of Contact process?
A. Pt
B. NiO
C. ZnO
D. V2O5
`
const INSTRUCTION = "Type your answer using the command <code>/ans [A/B/C/D]</code> in any group with @kaito_bot or dm her. GOGOGO!"

const ANSWER = "D"
const REPLY_TEXT = `
Answer: Check notes yourselves
Stealing champion: ` //<a href='https://t.me/system_logs/396'>Check here!</a>
const COMMAND = "/ANS "

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

  msg := tgbotapi.NewMessageToChannel(CHANNEL_NAME, QUESTION + INSTRUCTION)
  log.Printf("1")
  msg.ParseMode = tgbotapi.ModeHTML
  log.Printf("DOne")
  message, err := bot.Send(msg)
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

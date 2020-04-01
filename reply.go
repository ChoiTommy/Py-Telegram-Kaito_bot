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
<b>DISCUSSION</b>
#phys #heat
You are given a beaker of hot water, an electronic balance, a thermometer, a stirrer, a polystyrene cup and some crushed ice.
Mass of the hot water is <i>mw</i> and the specific heat capacity of water is <i>c</i>.
Describe an experiment to measure the specific latent heat of fusion of ice <i>lf</i>.
States your assumptions and suggest 2 physical quantities to be measured and the equation involved.

`
const INSTRUCTION = `Type your thoughts using the command
 <code>/ans [Your answer]</code> in any group with @kaito_bot or dm her.
 Use nerdy HTML tags to format your answer.
 Maximum 10 answers will be saved.`
const DIVIDE_LINE = `
--------------------
Your brilliant ideas💡:
`

var inlineButton = tgbotapi.NewInlineKeyboardMarkup(
	tgbotapi.NewInlineKeyboardRow(
		tgbotapi.NewInlineKeyboardButtonURL("Join Discussion","https://t.me/kaito_bot"),
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

  messageText := QUESTION + INSTRUCTION
  msg := tgbotapi.NewMessageToChannel(CHANNEL_NAME, messageText)
  msg.ParseMode = tgbotapi.ModeHTML
  msg.ReplyMarkup = inlineButton
  message, err := bot.Send(msg)
  log.Printf("Sent")

  u := tgbotapi.NewUpdate(0)
	u.Timeout = 60
	updates, err := bot.GetUpdatesChan(u)

  counter := 0
  messageText = messageText + DIVIDE_LINE

  for update := range updates {
    if update.Message == nil { // ignore any non-Message Updates
			continue
		}

    log.Printf("[%s] %s: %s", update.Message.From.UserName, update.Message.From.FirstName + update.Message.From.LastName, update.Message.Text)

    if update.Message.IsCommand() {
			switch update.Message.Command() {
			case "ans":
        text := "<b>" + update.Message.From.FirstName + update.Message.From.LastName + "</b> :" + strings.ReplaceAll(update.Message.Text, "/ans", " ")
        messageText = messageText + text + "\n"
        msg := tgbotapi.NewEditMessageText(message.Chat.ID, message.MessageID, messageText)
        msg.ParseMode = tgbotapi.ModeHTML
        bot.Send(msg)
        bot.Send(tgbotapi.NewEditMessageReplyMarkup(message.Chat.ID, message.MessageID, inlineButton))
        counter++

        msgReply := tgbotapi.NewMessage(update.Message.Chat.ID, "Your answers have been saved. Go to @system_logs again to see others' answers.")
  	    msgReply.ReplyToMessageID = update.Message.MessageID
  	    bot.Send(msgReply)
			default:
        msgReply := tgbotapi.NewMessage(update.Message.Chat.ID, "Belo")
  	    msgReply.ReplyToMessageID = update.Message.MessageID
  	    bot.Send(msgReply)
			}
		}
    if counter > 9 {break}
  }
  messageText = messageText + "Discussion ended."
  msgEnd := tgbotapi.NewEditMessageText(message.Chat.ID, message.MessageID, messageText)
  msgEnd.ParseMode = tgbotapi.ModeHTML
  bot.Send(msgEnd)
  log.Printf("Program end.")
}

package main
/* Meme bot
 * Source: https://github.com/go-telegram-bot-api/telegram-bot-api
 */
import (
	"log"
	"strings"
	"github.com/go-telegram-bot-api/telegram-bot-api"
)

func main() {
	bot, err := tgbotapi.NewBotAPI("")
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates, err := bot.GetUpdatesChan(u)

	list := [6]string{"偷", "練", "做", "睇", "食", "訓"}
	messages := [4]string{"%s完又%s", "日%s夜%s", "一%s再%s", "死%s爛%s"}

	for update := range updates {
		if update.Message == nil { // ignore any non-Message Updates
			continue
		}

		log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

		i := 0
		match := false
		for ((i <= 5) && !match) {
			match = strings.Contains(update.Message.Text, list[i])
			i++
		}

		if match {
			pending := ""
			for n := 0; n <= 3; n++ {
				pending = pending + strings.ReplaceAll(messages[n], "%s", list[i-1]) + "\n"
			}
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, pending)
			msg.ReplyToMessageID = update.Message.MessageID
			bot.Send(msg)
		}
	}
}

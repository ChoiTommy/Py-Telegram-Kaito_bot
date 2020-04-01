package main

import (
	"log"
        "fmt"
        "io/ioutil"
	"github.com/go-telegram-bot-api/telegram-bot-api"
)
const CHANNEL_NAME = "@system_logs"
const FILE_PATH = "key.txt"
var inlineButton = tgbotapi.NewInlineKeyboardMarkup(
	tgbotapi.NewInlineKeyboardRow(
		tgbotapi.NewInlineKeyboardButtonSwitch("2sw","open 2"),
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
  channelid := int64(-1001321795482);
	//bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)
  msg := tgbotapi.NewMessage(channelid, "messageText")
  msg.ReplyMarkup = inlineButton
  bot.Send(msg)

	fmt.Print(".")
}

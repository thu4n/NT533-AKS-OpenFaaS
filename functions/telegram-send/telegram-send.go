package function

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

type telegramParams struct {
	ChatID  string
	Message string
}

// sendToTelegram sends a message to chat with the passed ID from the passed telegram bot
func sendToTelegram(apiToken string, chatID string, message string) string {
	var sendTo = "https://api.telegram.org/bot" + apiToken + "/sendMessage?chat_id=" + chatID
	var messageTosend = "&text=" + message

	resp, err := http.Get(sendTo + messageTosend)
	if err != nil {
		log.Println("There was an error:", err)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Println("There was an error:", err)
	}

	return string(body)

}

func getAPISecret() (secretBytes []byte, err error) {
	// read from the openfaas secrets folder
	secretBytes, err = ioutil.ReadFile("/var/openfaas/secrets/secret-api-key")

	return secretBytes, err
}

// Handle the request
func Handle(req []byte) string {
	var params telegramParams
	err := json.Unmarshal(req, &params)

	if err != nil {
		log.Println("There was an error:", err)
	}

	secretBytes, err := getAPISecret()
	if err != nil {
		log.Fatal(err)
	}

	secret := strings.TrimSpace(string(secretBytes))

	var result = sendToTelegram(secret, params.ChatID, params.Message)
	return fmt.Sprintf(result)
}

package main

import (
	"fmt"
)

// Handler function
func Handle(name string) string {
	if name == "" {
		return "Hello from OpenFaas!"
	}
	return fmt.Sprintf("Hello, %s!", name)
}

func main() {
	// Entry point for the function, typically unused in OpenFaas
	fmt.Println("This is a dummy function for OpenFaas!")
}

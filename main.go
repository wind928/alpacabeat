package main

import (
	"os"

	"github.com/wind928/alpacabeat/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}

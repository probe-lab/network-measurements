// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Keep in sync with ../base64/example_test.go.

package main

import (
	"os"
	"log"
	"fmt"
	"bufio"
    "strings"
	"encoding/json"
	cid "github.com/ipfs/go-cid"
	b58 "github.com/mr-tron/base58/base58"
	base32 "github.com/multiformats/go-base32"
)

type ProviderRecord struct {
    Key string
    Value string
    Expiration string
    Size int
}

func DecodeString(s string) []byte {
	data, err := base32.RawStdEncoding.DecodeString(s)
	if err != nil {
		fmt.Println("error:", err)
		return  make([]byte, 2)
	}
	return data
}

func ParseRecord(providerRecord ProviderRecord) (string, string){
    cid_base32 :=  strings.Split(providerRecord.Key, "/")[2]
    peerid_base32 :=  strings.Split(providerRecord.Key, "/")[3]
    decoded_cid := DecodeString(cid_base32)
    decoded_pid := DecodeString(peerid_base32)
    if (decoded_cid[0] != 0){
        c, err := cid.Cast(decoded_cid)
        if err != nil {
            log.Println(err)
        }
        p := b58.Encode(decoded_pid)

    }
}



func main() {
	
	// Get the path to the file with the provider records
	providersFilepath := os.Args[1]
	// Open the file to read
	file, err := os.Open(providersFilepath)
    if err != nil {
        log.Fatal(err)
	}
	defer file.Close()

	// Open the output file
	fout, err := os.Create("provider_records.txt")
	if err != nil {
        log.Fatal(err)
	}
	defer fout.Close()
	writer := bufio.NewWriter(fout)

	// Read the input file line-by-line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		jsonString := scanner.Text()
		var providerRecord ProviderRecord	
		json.Unmarshal([]byte(jsonString), &providerRecord)
		c, p = ParseRecord(providerRecord)
		fmt.Fprintf(writer, "%v\t%v\t%v\n", p, c, providerRecord.Expiration)
	}
	writer.Flush()    
}
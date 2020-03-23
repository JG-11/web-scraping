const cheerio = require('cheerio')
const request = require('request-promise')


async function main() {
    const result = await request.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
    const $ = cheerio.load(result)

    console.log($("#confirmedCases").text())

    /*$("#labels_layer > text").each((index, element) => { 
        console.log($(element).text())
    })*/
}

main()
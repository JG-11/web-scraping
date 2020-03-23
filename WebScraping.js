const cheerio = require('cheerio')
const request = require('request-promise')


async function main() {
    const result = await request.get("https://www.worldometers.info/coronavirus/")
    const $ = cheerio.load(result)

    const scrapedData = []

    $("#main_table_countries_today > tbody > tr").each((index, element) => {
        const cells = $(element).find("td")
        const country = $(cells[0]).text()
        const totalCases = $(cells[1]).text()
        const newCases = $(cells[2]).text()
        const totalDeaths = $(cells[3]).text()

        const tableRow = { country, totalCases, newCases, totalDeaths }
        
        scrapedData.push(tableRow)
    })

    console.log(scrapedData)
}

main()

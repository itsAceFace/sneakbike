function gameReadmeRender(gameArray, console) {
  //game1, game2, game3
  var consoleLower = console.toLowerCase();

  let gameSections = [];
  for (const gameNum in gameArray) {
    const val = gameArray[gameNum];

    let hintSection = ``;
    if (val["hints"] && val["hints"].trim().length > 0) {
      hintSection = `<h2 class="hint">Hints and Tips</h2>

        <p class="hint">${val["hints"]}</p>
      `;
    }

    const gameAndObjSection = `
      <div class="game">
      <h1>Game ${parseInt(gameNum) + 1}</h1>
      <div class="box">
          <h2 class="objective">Objective</h2>
          <p class="objective">
             ${val["objective"]}
          </p>
          ${hintSection}
      </div>
      <br/>
      `;

    const endGameAndObjSection = `</div>`;
    const controlsSectionSNES = `
      <tr><td><b>A</b></td><td>${
        val["a"] == "" ? "&mdash;" : val["a"]
      }</td></tr>
      <tr><td><b>B</b></td><td>${
        val["b"] == "" ? "&mdash;" : val["b"]
      }</td></tr>
      <tr><td><b>X</b></td><td>${
        val["x"] == "" ? "&mdash;" : val["x"]
      }</td></tr>
      <tr><td><b>Y</b></td><td>${
        val["y"] == "" ? "&mdash;" : val["y"]
      }</td></tr>
      <tr><td><b>L</b></td><td>${
        val["l"] == "" ? "&mdash;" : val["l"]
      }</td></tr>
      <tr><td><b>R</b></td><td>${
        val["r"] == "" ? "&mdash;" : val["r"]
      }</td></tr>
      `;

    const controlsSectionNES = `
      <tr><td><b>A</b></td><td>${
        val["a"] == "" ? "&mdash;" : val["a"]
      }</td></tr>
      <tr><td><b>B</b></td><td>${
        val["b"] == "" ? "&mdash;" : val["b"]
      }</td></tr>
     `;

    const controlsSectionGenesis = `
      <tr><td><b>A</b></td><td>${
        val["a"] == "" ? "&mdash;" : val["a"]
      }</td></tr>
      <tr><td><b>B</b></td><td>${
        val["b"] == "" ? "&mdash;" : val["b"]
      }</td></tr>
      <tr><td><b>C</b></td><td>${
        val["c"] == "" ? "&mdash;" : val["c"]
      }</td></tr>
      <tr><td><b>X</b></td><td>${
        val["x"] == "" ? "&mdash;" : val["x"]
      }</td></tr>
      <tr><td><b>Y</b></td><td>${
        val["y"] == "" ? "&mdash;" : val["y"]
      }</td></tr>
      <tr><td><b>Z</b></td><td>${
        val["z"] == "" ? "&mdash;" : val["z"]
      }</td></tr>
      <tr><td><b>L</b></td><td>${
        val["l"] == "" ? "&mdash;" : val["l"]
      }</td></tr>
      <tr><td><b>R</b></td><td>${
        val["r"] == "" ? "&mdash;" : val["r"]
      }</td></tr>
      `;

    const controlSectionUniversal = `
      <tr><td><b>Start</b></td><td>${
        val["start"] == "" ? "&mdash;" : val["start"]
      }</td></tr>
      <tr><td><b>Select</b></td><td>${
        val["select"] == "" ? "&mdash;" : val["select"]
      }</td></tr>
      <tr><td><b>Up</b></td><td>${
        val["up"] == "" ? "&mdash;" : val["up"]
      }</td></tr>
      <tr><td><b>Down</b></td><td>${
        val["down"] == "" ? "&mdash;" : val["down"]
      }</td></tr>
      <tr><td><b>Left</b></td><td>${
        val["left"] == "" ? "&mdash;" : val["left"]
      }</td></tr>
      <tr><td><b>Right</b></td><td>${
        val["right"] == "" ? "&mdash;" : val["right"]
      }</td></tr>
      `;

    var controlSectionConsoleDict = {
      snes: controlsSectionSNES,
      nes: controlsSectionNES,
      genesis: controlsSectionGenesis,
    };

    var controlsSection = `<table>
    ${controlSectionConsoleDict[consoleLower]}
    ${controlSectionUniversal}
    </table>`;

    gameSections.push(
      gameAndObjSection + controlsSection + endGameAndObjSection
    );
  }

  return header + gameSections.join(" ") + endHtml;
}

const endHtml = `</div></html>`;

const header = `
  <!DOCTYPE html>

  <html lang="en">

  <head>
      <meta charset="utf-8" />
      <title>Sneakbike Games</title>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400&display=swap"
          rel="stylesheet" />
      <style>
          body {
              font-size: 14px;
              line-height: 1.2rem;
              font-family: "Roboto", sans-serif;
          }

          table {
              border-collapse: collapse;
              width: 500px;
              margin-bottom: 1.5rem;
          }

          table td {
              border: 1px solid #ddd;
              padding: 8px;
          }

          table tr:nth-child(even) {
              background-color: #f2f2f2;
          }

          table tr:hover {
              background-color: #ddd;
          }

          .box {
              border: solid 1px black;
              padding-left: 1rem;
              padding-right: 1rem;
              border-radius: 5px;
          }

          .hint {
              color: #777;
              font-weight: bold;
          }

          .objective {
              color: #ef5350;
              font-weight: bold;
          }

          .game {
              width: 500px;
              border: solid 2px black;
              padding: 1rem;
              border-radius: 5px;
              margin: 1rem;
          }

          .container {
              display: flex;
              flex-wrap: wrap;
          }
      </style>
  </head>
  <body>
    <div class="container">
`;

export default gameReadmeRender;

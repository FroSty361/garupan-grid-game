const guessArea = document.getElementById('guess-area');

guessArea.toggleAttribute('hidden');

const guessAreaInput = document.getElementById('character-guess-input');

guessAreaInput.addEventListener('input', (event) => {
    autoCheckCharacter(event);
});

const characterGuessNamesContainer = document.getElementById('character-guess-names');

const guessAreaExitButton = document.getElementById('guess-exit-button');

guessAreaExitButton.addEventListener('click', (event) => { // Turning Off View
    removeAutoCheckedCharacters()

    guessArea.toggleAttribute('hidden');
})

const guessButtons = document.querySelectorAll("button.guess-box");

guessButtons.forEach(guessButton => {
    guessButton.addEventListener('click', (event) => {
        onGuessButtonClicked(event);
    });
});

let currentBoxCoords = null;

function onGuessButtonClicked(event)
{
    const box = event.target;

    if (box.ariaLabel === "Empty cell")
    {
        currentBoxCoords = box.dataset.guessButtonCoord;

        guessArea.toggleAttribute('hidden');
    }

    currentBoxCoords = null;
}

function autoCheckCharacter(event)
{
    name = event.target.value

    const payload = { character_name: name };

     fetch('/api/game/check-character-name', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(payload)
     })
     .then(response => response.json())
     .then(data => {
        if (data.success)
        {
            processAutoCheckedCharacters(data.result);
        }
     })
     .catch(error => console.error('Error:', error));
}

function processAutoCheckedCharacters(characters)
{
    removeAutoCheckedCharacters()

    characters.forEach((character) => {
        createAutoCheckedCharacter(character);
    });
}

function createAutoCheckedCharacter(characterName)
{
    const character_html = `
        <div class="character-guess-name" data-character-guess-name="${characterName}">
            <p>${characterName}</p>
            <button>Guess</button>
        </div>
    `;

    characterGuessNamesContainer.insertAdjacentHTML("beforeend", character_html);
}

function removeAutoCheckedCharacters()
{
    const characters = document.querySelectorAll('.character-guess-name');

    characters.forEach(character => {
        character.remove()
    });
}

function guessCharacter()
{
    if (currentBoxCoords === null)
    {
        return;
    }

    alert("Hi!");
}
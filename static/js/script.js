document.getElementById('recommendationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const input = document.getElementById('preferences');
    const favoriteBook = input.value.trim();

    fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ favorite_book: favoriteBook })  
    })
    .then(response => response.json())
    .then(data => {
        console.log("Received data:", data);

        if (data.error) {
            document.getElementById('results').innerHTML = `<p>Error: ${data.error}</p>`;
            return;
        }

        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML =
            '<h2>Recommended Books:</h2><ul>' +
            data.recommendations.map(book => `<li>${book}</li>`).join('') +
            '</ul>';
    })
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('bookForm');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', async e => {
        e.preventDefault(); 

        const favoriteBook = document.getElementById('favoriteBook').value.trim();
        if (!favoriteBook) {
            resultsDiv.textContent = "Please enter a book name.";
            return;
        }

        resultsDiv.textContent = "Searching...";

        try {
            const res = await fetch('/get_similar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ favorite_book: favoriteBook })
            });

            const data = await res.json();
            const books = data.similar_books || [];

            if (books.length === 0) {
                resultsDiv.textContent = "No similar books found.";
                return;
            }

            // Create list of books
            resultsDiv.innerHTML = `<ul>${books.map(b => `<li>${b.title} by ${b.author}</li>`).join('')}</ul>`;
        } catch (err) {
            resultsDiv.textContent = "Error fetching books. Please try again.";
            console.error(err);
        }
    });
});

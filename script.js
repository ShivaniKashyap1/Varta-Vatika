document.addEventListener('DOMContentLoaded', function () {
    var searchButton = document.getElementById('searchButton');
    var searchInput = document.getElementById('searchInput');

    searchButton.addEventListener('click', function () {
        var searchTerm = searchInput.value.trim().toLowerCase();
        if (searchTerm !== '') {
            // Replace this with your own logic to find words on your website
            var contentParagraphs = document.querySelectorAll('.content p');
            contentParagraphs.forEach(function (paragraph) {
                var paragraphText = paragraph.textContent.toLowerCase();
                if (paragraphText.includes(searchTerm)) {
                    paragraph.style.background = 'yellow';
                }
            });
        } else {
            alert('Please enter a search term.');
        }
    });
});


const footer= document.getElementById('myFooter');
window.addEventListener('scroll', function(){
  const scrollPosition= window.pageYOffset || document.documentElement.scrollTop;
  const windowHeight= window.innerHeight || document.documentElement.clientHeight;
  const documentHeight= document.documentElement.scrollHeight;

if (scrollPosition + windowHeight >= documentHeight) {
    footer.style.display= 'block';
} else {
    footer.style.display= 'none';
}
});


// Get all files
const files = document.querySelectorAll('.file');

// For each file, add event listeners to the stars
files.forEach(file => {
    const stars = file.querySelectorAll('.star');
    let rating = 0;

    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            rating = index + 1;
            updateStars();
            calculateAverageRating();
        });
    });

    // Helper function to update the stars based on the current rating
    function updateStars() {
        stars.forEach((star, index) => {
            if (index < rating) {
                star.classList.add('filled');
            } else {
                star.classList.remove('filled');
            }
        });
    }

    // Helper function to calculate the average rating and update the display
    function calculateAverageRating() {
        const averageRatingSpan = file.querySelector(`#average-rating-${file.id}`);
        averageRatingSpan.textContent = rating;
        // You can add further logic here to calculate the mean of scorings
    }
});





// Using plain JavaScript
document.querySelector('.dropdown-toggle').addEventListener('click', function() {
  document.querySelector('.dropdown-menu').classList.toggle('show');
});

// Using jQuery
$('.dropdown-toggle').on('click', function() {
  $('.dropdown-menu').toggleClass('show');
});

let score = 0;
let timer;

$('.game__btn').on('click', function () {
    clearTimeout(timer);
    
    const selectedButton = $(this).data('index')
    const buttons = $(".game__btn").toArray();
    const correctButton = Math.floor(Math.random() * buttons.length) + 1;

    if (selectedButton === correctButton) {
        score++;
        $("#score").text(`${score}`);

        $(buttons).each(function () {
            const path = $(this).children().data("green");
            $(this).children().attr("src", path);
        });

        setTimeout(() => {
            $(buttons).each(function () {
                const path = $(this).children().data("normal");
                $(this).children().attr("src", path);
            });
        }, 1000);
    } else {
        $(buttons).each(function () {
            const path = $(this).children().data("red");
            $(this).children().attr("src", path);
        });

        setTimeout(() => {
            window.location.href = `/again?score=${score}`;
        }, 1000);
    }

    startTimer();
})

function startTimer() {
    let seconds = 9;

    timer = setInterval(() => {
        $("#timer").text(`00:0${seconds}`);

        if (seconds === 0) {
            clearInterval(timer);
            window.location.href = `/again?score=${score}`;
        } else {
            seconds--;
        }
    }, 900);
}

startTimer();

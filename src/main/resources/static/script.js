document.addEventListener("DOMContentLoaded", function() {
    const imageInput = document.getElementById('image');
    const answerPart = document.getElementById('answerPart');
    const preview = document.getElementById('preview');
    const answer = document.getElementById('answer');

    function checkFiles(files) {
        console.log(files);

        if (files.length != 1) {
            alert("Bitte genau eine Datei hochladen.");
            return;
        }

        const fileSize = files[0].size / 1024 / 1024; // in MiB
        if (fileSize > 10) {
            alert("Datei zu gross (max. 10Mb)");
            return;
        }

        answerPart.style.visibility = "visible";
        const file = files[0];

        // Preview
        if (file) {
            preview.src = URL.createObjectURL(file);
        }

        // Upload
        const formData = new FormData();
        formData.append("image", file);

        fetch('/analyze', {
            method: 'POST',
            headers: {},
            body: formData
        }).then(response => {
            console.log(response);
            return response.text();
        }).then(text => {
            answer.innerHTML = text;
        }).catch(error => {
            console.log(error);
            answer.innerHTML = "Error during image analysis.";
        });
    }

    function submitImage() {
        if (imageInput.files.length > 0) {
            checkFiles(imageInput.files);
        } else {
            alert("Bitte ein Bild auswählen.");
        }
    }

    // Trigger submitImage function when file is chosen
    imageInput.addEventListener('change', submitImage);
});

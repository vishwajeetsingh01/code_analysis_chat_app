let hasReview = false;

function handleFileUpload() {
    const fileInput = document.getElementById("codeFile");
    const uploadStatus = document.getElementById("uploadStatus");
    const file = fileInput.files[0];

    uploadStatus.innerHTML = `<br><div class="loader"></div> File Uploading...</span>`;

    const reader = new FileReader();
    reader.onload = function () {
        if (fileInput.files.length > 0) {
            uploadStatus.innerHTML = "<span style='color: green;'><br>✅ File successfully uploaded.</span>";
        } else {
            uploadStatus.innerHTML = "";
        }
    };
    reader.readAsText(file);
}


async function sendCode() {
    const fileInput = document.getElementById("codeFile");
    const responseBox = document.getElementById("responseBox");

    if (!fileInput.files.length) {
        hasReview = false;
        responseBox.innerHTML = "<span style='color: red;'>Please upload a code file before submitting for review.</span>";
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    responseBox.innerHTML = "<div class='loader'></div> Reviewing your code...";

    reader.onload = async function(event) {
        const code = event.target.result.trim();

        if (!code) {
            hasReview = false;
            responseBox.innerHTML = "<span style='color: red;'>Uploaded file is empty.</span>";
            return;
        }

        hasReview = false;

        try {
            const response = await fetch('/review', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: code })
            });

            const data = await response.json();
       
            if (data.response) {
                hasReview = true;
                uploadStatus.innerHTML = `<br><span style="color: green;">✅ Code successfully reviewed.</span>`;
                responseBox.innerHTML = marked.parse(data.response);
            } else {
                uploadStatus.innerHTML = "";
                responseBox.innerHTML = "Error: " + data.error;
            }
            
        } catch (error) {
            responseBox.innerHTML = "An error occurred while submitting the code.";
        }
    };
    reader.readAsText(file);
}

async function downloadPDF() {
    const responseBox = document.getElementById("responseBox");

    if (!hasReview) {
        responseBox.innerHTML = "<span style='color: red;'>No review available to download as PDF.</span>";
        return;
    }

    const element = responseBox.cloneNode(true);
    element.style.maxHeight = "unset";
    element.style.overflow = "visible";

    const opt = {
        margin:       0.5,
        filename:     'Code Review Report.pdf',
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };

    html2pdf().from(element).set(opt).save();
}

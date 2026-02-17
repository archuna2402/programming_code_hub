async function submitAnswers() {
    const response = await fetch("http://127.0.0.1:5000/api/submit_answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            level: 2,
            answers: [
                { answer: "Python is a programming language." },
                { answer: "We use print() to display output." },
                { answer: "A variable stores data." },
                { answer: "10 is an integer." },
                { answer: "A list stores multiple values." },
                { answer: "It is easy to learn." },
                { answer: "Used for web and AI." },
                { answer: "It is open source." }
            ]
        })
    });

    const data = await response.json();
    console.log(data);
}

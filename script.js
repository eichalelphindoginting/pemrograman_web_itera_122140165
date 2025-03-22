document.addEventListener("DOMContentLoaded", loadTodos);

function addTodo() {
    let input = document.getElementById("todo-input");
    let text = input.value.trim();
    if (text === "") return;

    let todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.push({ text, done: false });
    localStorage.setItem("todos", JSON.stringify(todos));

    input.value = "";
    renderTodos();
}

function renderTodos() {
    let list = document.getElementById("todo-list");
    list.innerHTML = "";
    let todos = JSON.parse(localStorage.getItem("todos")) || [];

    todos.forEach((todo, index) => {
        let li = document.createElement("li");
        li.textContent = todo.text;
        if (todo.done) {
            li.classList.add("completed");
        }

        let doneButton = document.createElement("button");
        doneButton.textContent = "Selesai";
        doneButton.classList.add("complete");
        doneButton.onclick = () => toggleDone(index);

        let deleteButton = document.createElement("button");
        deleteButton.textContent = "Hapus";
        deleteButton.classList.add("delete");
        deleteButton.onclick = () => deleteTodo(index);

        li.appendChild(doneButton);
        li.appendChild(deleteButton);
        list.appendChild(li);
    });
}

function toggleDone(index) {
    let todos = JSON.parse(localStorage.getItem("todos"));
    todos[index].done = !todos[index].done;
    localStorage.setItem("todos", JSON.stringify(todos));
    renderTodos();
}

function deleteTodo(index) {
    let todos = JSON.parse(localStorage.getItem("todos"));
    todos.splice(index, 1);
    localStorage.setItem("todos", JSON.stringify(todos));
    renderTodos();
}

function loadTodos() {
    renderTodos();
}

// Fungsi kalkulator dengan operasi tambahan
function hitungKalkulator(angka1, angka2, operasi) {
    let hasil = 0;
    switch (operasi) {
        case "tambah":
            hasil = angka1 + angka2;
            break;
        case "kurang":
            hasil = angka1 - angka2;
            break;
        case "kali":
            hasil = angka1 * angka2;
            break;
        case "bagi":
            if (angka2 === 0) {
                return "Error: Pembagian dengan nol tidak diperbolehkan";
            }
            hasil = angka1 / angka2;
            break;
        case "pangkat":
            hasil = Math.pow(angka1, angka2);
            break;
        case "akar":
            if (angka1 < 0) {
                return "Error: Tidak bisa menghitung akar kuadrat dari angka negatif";
            }
            hasil = Math.sqrt(angka1);
            break;
        case "modulus":
            hasil = angka1 % angka2;
            break;
        default:
            return "Operasi tidak valid";
    }
    return hasil;
}

// Tambahkan event listener untuk operasi tambahan
function setupKalkulator() {
    document.getElementById("btn-pangkat").addEventListener("click", function() {
        const angka1 = parseFloat(document.getElementById("angka1").value);
        const angka2 = parseFloat(document.getElementById("angka2").value);
        const hasil = hitungKalkulator(angka1, angka2, "pangkat");
        document.getElementById("hasil-kalkulator").innerHTML = `<p>Hasil: ${angka1} ^ ${angka2} = ${hasil}</p>`;
    });

    document.getElementById("btn-akar").addEventListener("click", function() {
        const angka1 = parseFloat(document.getElementById("angka1").value);
        const hasil = hitungKalkulator(angka1, 0, "akar");
        document.getElementById("hasil-kalkulator").innerHTML = `<p>Hasil: √${angka1} = ${hasil}</p>`;
    });

    document.getElementById("btn-modulus").addEventListener("click", function() {
        const angka1 = parseFloat(document.getElementById("angka1").value);
        const angka2 = parseFloat(document.getElementById("angka2").value);
        const hasil = hitungKalkulator(angka1, angka2, "modulus");
        document.getElementById("hasil-kalkulator").innerHTML = `<p>Hasil: ${angka1} % ${angka2} = ${hasil}</p>`;
    });
}

document.addEventListener("DOMContentLoaded", setupKalkulator);

document.getElementById("registration-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Mencegah form dikirim jika ada error

    let isValid = true;

    // Validasi Nama
    const nama = document.getElementById("nama").value.trim();
    const errorNama = document.getElementById("error-nama");
    if (nama.length < 3) {
        errorNama.textContent = "Nama harus lebih dari 3 karakter!";
        isValid = false;
    } else {
        errorNama.textContent = "";
    }

    // Validasi Email
    const email = document.getElementById("email").value.trim();
    const errorEmail = document.getElementById("error-email");
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Pola email valid
    if (!emailPattern.test(email)) {
        errorEmail.textContent = "Email tidak valid!";
        isValid = false;
    } else {
        errorEmail.textContent = "";
    }

    // Validasi Password
    const password = document.getElementById("password").value.trim();
    const errorPassword = document.getElementById("error-password");
    if (password.length < 8) {
        errorPassword.textContent = "Password harus minimal 8 karakter!";
        isValid = false;
    } else {
        errorPassword.textContent = "";
    }

    // Jika semua validasi lolos
    if (isValid) {
        document.getElementById("success-message").textContent = "Pendaftaran berhasil!";
        document.getElementById("registration-form").reset(); // Mengosongkan form
    }
});

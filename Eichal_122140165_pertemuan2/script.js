class ListManager {
    constructor(type, formId, inputId, listId) {
      this.type = type;
      this.storageKey = `${type}s`;
      this.data = this.loadData();
      this.form = document.getElementById(formId);
      this.input = document.getElementById(inputId);
      this.list = document.getElementById(listId);
      this.init();
    }
  
    init = () => {
      this.render();
      this.form.addEventListener("submit", this.addItem);
    };
  
    loadData = () => {
      return JSON.parse(localStorage.getItem(this.storageKey)) || [];
    };
  
    saveData = () => {
      localStorage.setItem(this.storageKey, JSON.stringify(this.data));
    };
  
    render = () => {
      this.list.innerHTML = "";
      this.data.forEach((item, index) => {
        let element;
  
        if (this.type === "note") {
          element = document.createElement("div");
          element.classList.add("memo");
          element.innerHTML = `
            <p>${item}</p>
            <button onclick="managers['${this.type}'].deleteItem(${index})">Hapus</button>
          `;
        } else {
          element = document.createElement("li");
          element.innerHTML = `
            <span>${item}</span>
            <button onclick="managers['${this.type}'].editItem(${index})">Edit</button>
            <button onclick="managers['${this.type}'].deleteItem(${index})">Hapus</button>
          `;
        }
  
        this.list.appendChild(element);
      });
    };
  
    addItem = (e) => {
      e.preventDefault();
      const value = this.input.value.trim();
      if (!value) return;
      this.data.push(value);
      this.saveData();
      this.input.value = "";
      this.render();
    };
  
    editItem = (index) => {
      const newText = prompt(`Edit ${this.type}:`, this.data[index]);
      if (newText !== null) {
        this.data[index] = newText.trim();
        this.saveData();
        this.render();
      }
    };
  
    deleteItem = (index) => {
      this.data.splice(index, 1);
      this.saveData();
      this.render();
    };
  }
  
  const managers = {
    note: new ListManager("note", "note-form", "note-input", "note-list"),
    schedule: new ListManager("schedule", "schedule-form", "schedule-input", "schedule-list"),
    task: new ListManager("task", "task-form", "task-input", "task-list"),
    todo: new ListManager("todo", "todo-form", "todo-input", "todo-list"),
  };
  
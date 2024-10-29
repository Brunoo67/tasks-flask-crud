from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

#CRUD - CREATE - READ - UPDATE - DELETE 

#TABELA: Tarefa

tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control #automaticamente a função vai ter acesso a variavel task_id_control (global pega a referencia que está fora do metodo), se criasse dentro do metodo, toda requisição ela seria 1.
    data = request.get_json()
    new_task = Task(id= task_id_control,
                    title=data.get("title"), 
                    description=data.get("description", "")) # "" torna o padrão vazio, podendo criar task sem description
    
    task_id_control +=1
    tasks.append(new_task)
    
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks] #mesmo for comentado abaixo
    #for task in tasks:
    #    task_list.append(task.to_dict())
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
                }

    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"]) #<int:id> é um identificador - parametro de rota.
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"Message" : "Não foi possível encontrar a atividade"}), 404


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if task == None:
        return jsonify({"Message" : "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"Message" : "Tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if task == None:
        return jsonify({"Message" : "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)

    return jsonify({"Message" : "Tarefa deletada com sucesso"})

        


if __name__ == "__main__": #recomendado em desenvolvimento local (executado de forma manual)
    app.run(debug=True)

import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    print('[bold green]ChatGPT API en Python[/bold green]')

    table = Table('Comando', 'Descripcion')
    table.add_row('exit','Salir de la aplicacion')
    table.add_row('new','Crear una nueva conversacion')

    print(table)

    # Contexto del asistente
    context = {'role':'system',
                'content':"eres un especialista ginecologia y dermatologia que trata y previene enfermedades genitales  "}
    messages = [context]

    while True:

        content = __prompt()

        if content == 'new':
            print('Nueva conversación creada')
            messages = [context]
            content = __prompt()
        

        messages.append({'role':'user','content':content})

        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo', messages = messages)#.choices[0]
        
        response_content = response.choices[0].message.content

        messages.append({'role':'assistant','content':response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
        prompt = typer.prompt('\n¿Sobre que quieres hablar? ')

        if prompt == 'exit':
            exit = typer.confirm('¿Estas seguro de salir?')
            if exit:
                print('¡Hasta luego!')
                raise typer.Abort()
            
            return __prompt()

        return prompt

if __name__ == "__main__":
    typer.run(main)


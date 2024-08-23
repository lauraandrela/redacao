from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

gemini.configure(api_key="AIzaSyA_K0y_2Pmp-JNBmmxJR60-9eplbgd6Liw")

model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/redacao', methods=['POST'])
def write_redacao():
    try:
    # ...
        dados = request.json
        criterios = dados.get('criterios')
        prompt = f"""
            Crie uma redação com os seguintes critérios: 
Apresente a redação no formato html com codificação UTF-8, sem o header, a estrutura que desejo é a seguinte:  
- A redação deve ser escrita dentro dos limites estruturais do texto dissertativo-argumentativo em prosa. Se atente para a organização do texto, expondo argumentos consistentes e defesa do ponto de vista, conectando os períodos através de conectivos (conjunções, advérbios, locuções, preposições, etc.).
- No primeiro parágrafo, você precisa apresentar o tema ao leitor. Você também precisa apresentá-los seu ponto de vista através de uma tese e pode itilizar algum tipo de repertório cultural (filme, livro, série).   
- No segundo parágrafo você precisa mostrar alguns argumentos que comprovem seu ponto de vista, para isso você deve utilizar algumas pesquisas, notícias, filmes, livros, pensadores, etc para relacionar e comprovar sua visão. Lembre-se de citar onde você obteve a informação. 
- No terceiro parágrafo adicione mais argumentos a favor de sua tese.  
- No final, você precisa concluir escrevendo uma proposta de intervenção, que esteja relacionada com seus argumentos, ou seja, apresentar o que é possível fazer, e mostrar: quem vai resolver, o que será feito, como será feito e qual o impacto da sua solução para o problema. Não seja muito detalhista, escreva a proposta com poucas frases.   
Observações:  
- Se a matéria, o tema e a tese não estiverem dentro de um contexto acadêmico e sério não gere a redação, se estiver relacionado a palavras torpes ou desrespeitosas e fora de um contexto sério, acadêmico ou profissional.
- O texto será escrito em português brasileiro.  
- Você precisa usar a linguagem formal, respeitando: vocabulário, regras de acentuação e pontuação, ortografia, separação de sílabas, usos do hífen e de letras maiúsculas e minúsculas, concordância, regência, ausência de marcas da oralidade.
- Você não pode desrespeitar os direitos humanos.  
- Existem algumas habilidades que serão avaliadas como: conhecimento sobre o tema, coerência, coesão, boa estrutura em  seus parágrafos e frases, boa argumentação, etc.  
- você precisa ser impessoal  
- Use a terceira pessoa  
- Não cite o texto que digitei como prompt 
Os respectivos critérios de matéria, tema proposto e tese são: {criterios}.

            """
        resposta = model.generate_content(prompt, generation_config = gemini.GenerationConfig (temperature=2))
        print(resposta)

        # Extrai a receita do texto da resposta
        redacao = resposta.text.strip().split('\n')
        return(redacao), 200 

    except Exception as e:
        return jsonify({"Erro": str(e)}), 300

if __name__ == '__main__':
    app.run(debug=True)
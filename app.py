from beam import App, Runtime, Image

app = App(
    name="custom-image",
    runtime=Runtime(
        cpu=1,
        memory="4Gi",
        # gpu="T4",
        image=Image(
            python_version="python3.9",
            # python_packages=[
            #     "transformers",
            #     "torch",
            # ],  # You can also add a path to a requirements.txt instead
            # base_image="ubuntu:20.04",
            commands=[''' \ 
              apt-get update && \ 
              apt-get install -y blender
            '''],
        ),
    ),
)

@app.rest_api()
def predict(**inputs):
    # model = OPTForCausalLM.from_pretrained("facebook/opt-125m")
    # tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")

    # prompt = inputs["prompt"]
    # inputs = tokenizer(prompt, return_tensors="pt")

    # # Generate
    # generate_ids = model.generate(inputs.input_ids, max_length=30)
    # result = tokenizer.batch_decode(
    #     generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    # )[0]

    # print(result)
    result = ""

    return {"prediction": result}

import util
import argparse
import sys
from tqdm import tqdm
import os
import pandas as pd


def main():
    
    parser = argparse.ArgumentParser("POS Tagging quechua")
    parser.add_argument("-t", "--train", help="Dataset de entrenamiento en formato csv", 
        default=None)
    parser.add_argument("-e", "--evaluation", help="Dataset de evaluación en formato csv", default=None)
    parser.add_argument("-u", "--usage", help="Utilizando un archivo csv", default=None)
    parser.add_argument("-i", "--interactive", help="utilizar en modo interactivo", action='store_true')
    parser.add_argument("-o", "--output", help="Archivo csv procesado", default=None)
    args = parser.parse_args()

    root_train = args.train
    root_eval = args.evaluation
    root_usage = args.usage
    root_out = args.output
    
    if args.train and args.evaluation:
        print("Proceso de entrenamiento y evaluación")
        util.train(root_train, root_eval, root_out)
        print("Proceso terminado")
    elif args.interactive:
        print("Introduzca la oración a procesar (escriba 0 para salir):")
        while True:
            in_sent = input()
            if in_sent == '0':
                sys.exit()
            print(util.use_huggingface(in_sent))
            print("\n")
            print("Introduzca la oración a procesar (escriba 0 para salir):")
    elif args.usage and args.output:
        print("Leyendo el archivo csv")
        df = pd.read_csv(root_usage, sep="\t")
        ner_iter = df["text"]
        ner_quechua = []
        print("Procesando archivo csv")
        with tqdm(total=len(ner_iter)) as pbar:
            for in_sent in ner_iter:
                ner_quechua.append(util.use_huggingface(in_sent))
                pbar.update(1)
        df["NER"] = ner_quechua
        print("Guardando csv procesado")
        df.to_csv(args.output+"data_pro.csv", sep='\t', index=False)
        print("Proceso terminado")


if __name__ == '__main__':
    main()

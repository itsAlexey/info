using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;

namespace CaesarWithKnife
{
    class Caesar
    {
        static void Main(string[] args)
        {
            string path = @"/Users/alex/Projects/caesarShitSharp/WarAndWorld.txt";

            File.Delete(path);/*) {
                Console.WriteLine(path);
            }*/

            Console.Write("Ключевое слово: ");
            string keyWord = Console.ReadLine().ToLower();
            Console.Write("Ключ: ");
            int key = Convert.ToInt32(Console.ReadLine());

            Caesar.createNewAlpha(keyWord, key);
            Console.WriteLine();
            Console.WriteLine("Шифрованный алфавит: " + Caesar.getNewAlpha());
            Console.WriteLine();

            string open = "", close = "";
            Console.Write("Открытое сообщение: ");
            open = Console.ReadLine().ToLower();
            close = Caesar.encrypt(open);
            Console.WriteLine();
            Console.WriteLine("Шифрованное сообщение: " + close);
            open = Caesar.decrypt(close);
            Console.WriteLine();
            Console.WriteLine("Расшифрованное сообщение: " + open);

            Console.ReadKey();
        }

        private static string alpha = "abcdefghijklmnopqrstuvwxyz";
        private static char[] newAlpha = new char[26];

        public static string encrypt(string Message)
        {
            string res = "";
            foreach (char ch in Message)
            {
                for (int i = 0; i < alpha.Length; i++)
                {
                    if (ch == alpha[i])
                    {
                        res += newAlpha[i];
                        break;
                    }
                }
            }
            return res;
        }

        public static string decrypt(string Message)
        {
            string res = "";
            foreach (char ch in Message)
            {
                for (int i = 0; i < newAlpha.Length; i++)
                {
                    if (ch == newAlpha[i])
                    {
                        res += alpha[i];
                        break;
                    }
                }
            }
            return res;
        }

        public static void createNewAlpha(string keyWord, int key) // создаёт новый алфавит с помощью ключа
        {
            bool findSame = false;
            key--;
            int beg = 0, current = key;
            // добавить ключевое слово в новый алфавит
            for (int i = key; i < keyWord.Length + key; i++)
            {
                for (int j = key; j < keyWord.Length + key; j++)
                {
                    if (keyWord[i - key] == newAlpha[j])
                    {
                        findSame = true;
                        break;
                    }
                }
                if (!findSame)// если повторений нету, то буква добавляется в новый алфавит
                {
                    newAlpha[current] = keyWord[i - key];
                    current++;
                }
                findSame = false;
            }

            // добавить буквы после ключевого слова
            for (int i = 0; i < alpha.Length; i++)
            {
                for (int j = 0; j < newAlpha.Length; j++)
                {
                    if (alpha[i] == newAlpha[j])
                    {
                        findSame = true;
                        break;
                    }
                }
                if (!findSame)
                {
                    newAlpha[current] = alpha[i];
                    current++;
                }
                findSame = false;
                if (current == newAlpha.Length)
                {
                    beg = i;
                    break;
                }
            }

            // добавить буквы после ключевого слова
            current = 0;
            for (int i = beg; i < alpha.Length; i++)
            {
                for (int j = 0; j < newAlpha.Length; j++)
                {
                    if (alpha[i] == newAlpha[j])
                    {
                        findSame = true;
                        break;
                    }
                }
                if (!findSame)
                {
                    newAlpha[current] = alpha[i];
                    current++;
                }
                findSame = false;
            }
        }

        public static string getNewAlpha()
        {
            string strNewAlpha = new string(newAlpha);
            return strNewAlpha;
        }
    }
}

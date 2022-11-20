import unittest
from bnlp import POS
from bnlp import NER
from bnlp import NLTKTokenizer
from bnlp import BasicTokenizer
from bnlp import SentencepieceTokenizer
from bnlp import BengaliWord2Vec
from bnlp.corpus import stopwords


class TestBNLP(unittest.TestCase):
    def test_BT(self):
        bt = BasicTokenizer()
        text = "আমি ভাত খাই।"
        tokens = bt.tokenize(text)
        self.assertEqual(tokens, ["আমি", "ভাত", "খাই", "।"])

        text1 = """
        ভারত থেকে অনুপ্রবেশ ঠেকাতে বর্ডার গার্ড বাংলাদেশের (বিজিবি)
         সঙ্গে রাজশাহীর চরখানপুর সীমান্ত পাহারা দিচ্ছেন গ্রামবাসী।
         সীমান্তে নজরদারি জোরদার করার জন্য     চরখানপুর গ্রামের প্রায় আড়াই শ
         বাসিন্দা রাত জেগে পালাক্রমে এই কাজ করছেন গত ২৮ নভেম্বর থেকে।
        """
        tokens1 = bt.tokenize(text1)
        output_1 = [
            "ভারত",
            "থেকে",
            "অনুপ্রবেশ",
            "ঠেকাতে",
            "বর্ডার",
            "গার্ড",
            "বাংলাদেশের",
            "(",
            "বিজিবি",
            ")",
            "সঙ্গে",
            "রাজশাহীর",
            "চরখানপুর",
            "সীমান্ত",
            "পাহারা",
            "দিচ্ছেন",
            "গ্রামবাসী",
            "।",
            "সীমান্তে",
            "নজরদারি",
            "জোরদার",
            "করার",
            "জন্য",
            "চরখানপুর",
            "গ্রামের",
            "প্রায়",
            "আড়াই",
            "শ",
            "বাসিন্দা",
            "রাত",
            "জেগে",
            "পালাক্রমে",
            "এই",
            "কাজ",
            "করছেন",
            "গত",
            "২৮",
            "নভেম্বর",
            "থেকে",
            "।",
        ]
        self.assertEqual(tokens1, output_1)

    def test_NLTK(self):
        text1 = """
        ভারত থেকে অনুপ্রবেশ ঠেকাতে বর্ডার গার্ড বাংলাদেশের (বিজিবি)
         সঙ্গে রাজশাহীর চরখানপুর সীমান্ত পাহারা দিচ্ছেন গ্রামবাসী।
         সীমান্তে নজরদারি জোরদার করার জন্য     চরখানপুর গ্রামের প্রায় আড়াই শ
         বাসিন্দা রাত জেগে পালাক্রমে এই কাজ করছেন গত ২৮ নভেম্বর থেকে।
        """
        text2 = "আমি ভাত খাই। সে বাজারে যায়। কী বলছো এসব?"

        gt_word_tokens = [
            "ভারত",
            "থেকে",
            "অনুপ্রবেশ",
            "ঠেকাতে",
            "বর্ডার",
            "গার্ড",
            "বাংলাদেশের",
            "(",
            "বিজিবি",
            ")",
            "সঙ্গে",
            "রাজশাহীর",
            "চরখানপুর",
            "সীমান্ত",
            "পাহারা",
            "দিচ্ছেন",
            "গ্রামবাসী",
            "।",
            "সীমান্তে",
            "নজরদারি",
            "জোরদার",
            "করার",
            "জন্য",
            "চরখানপুর",
            "গ্রামের",
            "প্রায়",
            "আড়াই",
            "শ",
            "বাসিন্দা",
            "রাত",
            "জেগে",
            "পালাক্রমে",
            "এই",
            "কাজ",
            "করছেন",
            "গত",
            "২৮",
            "নভেম্বর",
            "থেকে",
            "।",
        ]

        gt_sen_tokens = ["আমি ভাত খাই।", "সে বাজারে যায়।", "কী বলছো এসব?"]
        nl = NLTKTokenizer()
        out_word_tokens = nl.word_tokenize(text1)
        self.assertEqual(out_word_tokens, gt_word_tokens)

        nl2 = NLTKTokenizer()
        out_sen_tokens = nl2.sentence_tokenize(text2)
        self.assertEqual(out_sen_tokens, gt_sen_tokens)

    def test_POS(self):
        bn_pos = POS()
        model_path = "model/bn_pos.pkl"
        text = "আমি ভাত খাই।"
        res = bn_pos.tag(model_path, text)
        self.assertEqual(
            res, [("আমি", "PPR"), ("ভাত", "NC"), ("খাই", "VM"), ("।", "PU")]
        )

    def test_NER(self):
        bn_ner = NER()
        model_path = "model/bn_ner.pkl"
        text = "সে ঢাকায় থাকে।"
        res = bn_ner.tag(model_path, text)
        self.assertEqual(res, [("সে", "O"), ("ঢাকায়", "S-LOC"), ("থাকে", "O")])

    def test_stopwords(self):
        self.assertEqual(
            stopwords,
            [
                "অতএব",
                "অথচ",
                "অথবা",
                "অনুযায়ী",
                "অনেক",
                "অনেকে",
                "অনেকেই",
                "অন্তত",
                "অন্য",
                "অবধি",
                "অবশ্য",
                "অর্থাত",
                "আই",
                "আগামী",
                "আগে",
                "আগেই",
                "আছে",
                "আজ",
                "আদ্যভাগে",
                "আপনার",
                "আপনি",
                "আবার",
                "আমরা",
                "আমাকে",
                "আমাদের",
                "আমার",
                "আমি",
                "আর",
                "আরও",
                "ই",
                "ইত্যাদি",
                "ইহা",
                "উচিত",
                "উত্তর",
                "উনি",
                "উপর",
                "উপরে",
                "এ",
                "এঁদের",
                "এঁরা",
                "এই",
                "একই",
                "একটি",
                "একবার",
                "একে",
                "এক্",
                "এখন",
                "এখনও",
                "এখানে",
                "এখানেই",
                "এটা",
                "এটাই",
                "এটি",
                "এত",
                "এতটাই",
                "এতে",
                "এদের",
                "এব",
                "এবং",
                "এবার",
                "এমন",
                "এমনকী",
                "এমনি",
                "এর",
                "এরা",
                "এল",
                "এস",
                "এসে",
                "ঐ",
                "ও",
                "ওঁদের",
                "ওঁর",
                "ওঁরা",
                "ওই",
                "ওকে",
                "ওখানে",
                "ওদের",
                "ওর",
                "ওরা",
                "কখনও",
                "কত",
                "কবে",
                "কমনে",
                "কয়েক",
                "কয়েকটি",
                "করছে",
                "করছেন",
                "করতে",
                "করবে",
                "করবেন",
                "করলে",
                "করলেন",
                "করা",
                "করাই",
                "করায়",
                "করার",
                "করি",
                "করিতে",
                "করিয়া",
                "করিয়ে",
                "করে",
                "করেই",
                "করেছিলেন",
                "করেছে",
                "করেছেন",
                "করেন",
                "কাউকে",
                "কাছ",
                "কাছে",
                "কাজ",
                "কাজে",
                "কারও",
                "কারণ",
                "কি",
                "কিংবা",
                "কিছু",
                "কিছুই",
                "কিন্তু",
                "কী",
                "কে",
                "কেউ",
                "কেউই",
                "কেখা",
                "কেন",
                "কোটি",
                "কোন",
                "কোনও",
                "কোনো",
                "ক্ষেত্রে",
                "কয়েক",
                "খুব",
                "গিয়ে",
                "গিয়েছে",
                "গিয়ে",
                "গুলি",
                "গেছে",
                "গেল",
                "গেলে",
                "গোটা",
                "চলে",
                "চান",
                "চায়",
                "চার",
                "চালু",
                "চেয়ে",
                "চেষ্টা",
                "ছাড়া",
                "ছাড়াও",
                "ছিল",
                "ছিলেন",
                "জন",
                "জনকে",
                "জনের",
                "জন্য",
                "জন্যওজে",
                "জানতে",
                "জানা",
                "জানানো",
                "জানায়",
                "জানিয়ে",
                "জানিয়েছে",
                "জে",
                "জ্নজন",
                "টি",
                "ঠিক",
                "তখন",
                "তত",
                "তথা",
                "তবু",
                "তবে",
                "তা",
                "তাঁকে",
                "তাঁদের",
                "তাঁর",
                "তাঁরা",
                "তাঁাহারা",
                "তাই",
                "তাও",
                "তাকে",
                "তাতে",
                "তাদের",
                "তার",
                "তারপর",
                "তারা",
                "তারৈ",
                "তাহলে",
                "তাহা",
                "তাহাতে",
                "তাহার",
                "তিনঐ",
                "তিনি",
                "তিনিও",
                "তুমি",
                "তুলে",
                "তেমন",
                "তো",
                "তোমার",
                "থাকবে",
                "থাকবেন",
                "থাকা",
                "থাকায়",
                "থাকে",
                "থাকেন",
                "থেকে",
                "থেকেই",
                "থেকেও",
                "দিকে",
                "দিতে",
                "দিন",
                "দিয়ে",
                "দিয়েছে",
                "দিয়েছেন",
                "দিলেন",
                "দু",
                "দুই",
                "দুটি",
                "দুটো",
                "দেওয়া",
                "দেওয়ার",
                "দেওয়া",
                "দেখতে",
                "দেখা",
                "দেখে",
                "দেন",
                "দেয়",
                "দ্বারা",
                "ধরা",
                "ধরে",
                "ধামার",
                "নতুন",
                "নয়",
                "না",
                "নাই",
                "নাকি",
                "নাগাদ",
                "নানা",
                "নিজে",
                "নিজেই",
                "নিজেদের",
                "নিজের",
                "নিতে",
                "নিয়ে",
                "নিয়ে",
                "নেই",
                "নেওয়া",
                "নেওয়ার",
                "নেওয়া",
                "নয়",
                "পক্ষে",
                "পর",
                "পরে",
                "পরেই",
                "পরেও",
                "পর্যন্ত",
                "পাওয়া",
                "পাচ",
                "পারি",
                "পারে",
                "পারেন",
                "পি",
                "পেয়ে",
                "পেয়্র্",
                "প্রতি",
                "প্রথম",
                "প্রভৃতি",
                "প্রযন্ত",
                "প্রাথমিক",
                "প্রায়",
                "প্রায়",
                "ফলে",
                "ফিরে",
                "ফের",
                "বক্তব্য",
                "বদলে",
                "বন",
                "বরং",
                "বলতে",
                "বলল",
                "বললেন",
                "বলা",
                "বলে",
                "বলেছেন",
                "বলেন",
                "বসে",
                "বহু",
                "বা",
                "বাদে",
                "বার",
                "বি",
                "বিনা",
                "বিভিন্ন",
                "বিশেষ",
                "বিষয়টি",
                "বেশ",
                "বেশি",
                "ব্যবহার",
                "ব্যাপারে",
                "ভাবে",
                "ভাবেই",
                "মতো",
                "মতোই",
                "মধ্যভাগে",
                "মধ্যে",
                "মধ্যেই",
                "মধ্যেও",
                "মনে",
                "মাত্র",
                "মাধ্যমে",
                "মোট",
                "মোটেই",
                "যখন",
                "যত",
                "যতটা",
                "যথেষ্ট",
                "যদি",
                "যদিও",
                "যা",
                "যাঁর",
                "যাঁরা",
                "যাওয়া",
                "যাওয়ার",
                "যাওয়া",
                "যাকে",
                "যাচ্ছে",
                "যাতে",
                "যাদের",
                "যান",
                "যাবে",
                "যায়",
                "যার",
                "যারা",
                "যিনি",
                "যে",
                "যেখানে",
                "যেতে",
                "যেন",
                "যেমন",
                "র",
                "রকম",
                "রয়েছে",
                "রাখা",
                "রেখে",
                "লক্ষ",
                "শুধু",
                "শুরু",
                "সঙ্গে",
                "সঙ্গেও",
                "সব",
                "সবার",
                "সমস্ত",
                "সম্প্রতি",
                "সহ",
                "সহিত",
                "সাধারণ",
                "সামনে",
                "সি",
                "সুতরাং",
                "সে",
                "সেই",
                "সেখান",
                "সেখানে",
                "সেটা",
                "সেটাই",
                "সেটাও",
                "সেটি",
                "স্পষ্ট",
                "স্বয়ং",
                "হইতে",
                "হইবে",
                "হইয়া",
                "হওয়া",
                "হওয়ায়",
                "হওয়ার",
                "হচ্ছে",
                "হত",
                "হতে",
                "হতেই",
                "হন",
                "হবে",
                "হবেন",
                "হয়",
                "হয়তো",
                "হয়নি",
                "হয়ে",
                "হয়েই",
                "হয়েছিল",
                "হয়েছে",
                "হয়েছেন",
                "হল",
                "হলে",
                "হলেই",
                "হলেও",
                "হলো",
                "হাজার",
                "হিসাবে",
                "হৈলে",
                "হোক",
                "হয়",
            ],
        )


if __name__ == "__main__":
    unittest.main()

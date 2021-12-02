from electrum_onion.plugins.revealer.revealer import RevealerPlugin

from . import ElectrumTestCase


class TestRevealer(ElectrumTestCase):

    def test_version_0_noisemap(self):
        versioned_seed = RevealerPlugin.get_versioned_seed_from_user_input('03b0c557d6d0d4308a3393851d78bd8c7861')
        noise_map = RevealerPlugin.get_noise_map(versioned_seed)
        bigint = 0
        for (x, y), pixel in noise_map.items():
            if pixel:
                bigint |= 1 << (y*RevealerPlugin.SIZE[1]+x)
        self.assertEqual(0x541dde00b20ac7d320510e943d7ed9ffff5ff6b431c915353fbeffbc1beb737ff3a59c032a39ff8cbd532dffe42655bccbbef4f777ffeff8ec90e64aacbff5f4ff37ef4f32ac1d7240ed2bbb37dfeff459c7c2e2e0bfddffff7fffc7fd27eeb84a5ceafcf6bf9ffaff632367f97fffbf9fbfecff2b3a11a1c5befdfbfe7f125fba2c3e5d4ded591f9fbbbadbeed2220fb4337df9e4c7bfbe6ce4ad7b18ad57f3d75dfe7b6deb7350478bdbf7b7bfdf776eb301217d1f5c7f7ffffeefffe2070f52dbedfff2fef7f27f7d27f80b6a7bfb7f67bcbf7faf11f6b577dfbefebd44ffffe7bf5ee17ba4fb3377e1fcffeded781eca37a5bff3ebefdccbe1538c16129aed7fadfd7eb3bab55bcbdaee7e5d5b9fff57bd662333923b27af4f4da5ffd8bb15b58effed8bbeeff9ab7ecb75b62b977fdd88f3fbaeef6997a999b4dfffbfa375bf9e9c12b6011e2fde9fef7f66efc1155cc4fedfeefffeeff6ded645712b12bfe2b35df796f7ca05e0f12afbff6fefd1dd7f736bb9a567dff5797eafc1bfa0cf6cd090ddddfbfb79fd9f7f17bba2197e5dd3fb7fd9ff7579f0b6e28f7df3bdfe6fa8efd5a0a2e48f4d6efff79bf5efebc2638ff7eefffbbdfdb5bfac80426052df6fe6fd33eff5336a3c87c9fcff797b6bddbf91fea62e635333ffd7bfdd35f5c365432f5dfe7fd8bfb6c6e7cc90e6b5796d1dfeef567fdf390124a4bfeefd7efd1eee7f88ca45658fbf5cabffbfebf9fefe2c9f73dbffd36d7df77d73665c5f1dfa7b5b7fffafb6ea18bf9396e37b77fffffffb6aefdb0635ff7e43cfeef77fd8a527741dd3fffef1eddedf7f4259cc4253ffd9dffffb3bfbb0632d3d7fbf7bfbbfedfff2a7589be7624faffffbdbd7dfb5b5189b66fde8abf8bfbba7f440b80c2ba86de5fdfdf7ffba25625877fb9fdbf6f39333fe20e7710cdffadef8e7fb727d059237ef3dfceb9bd7ffef7b041565f2bb7ffdfefffff1ba3c7abb9a0fcf3fdf78fee7efb5da83dd1ffadebde675ff36d725426027dfffd9f76df3f7605b7f6fa4f75ff6e3df57ffd1a56c6239feffebffeecffdbd1ecc69f99ffea7f5ec759e2b2a99977b467edbffafae5faef9e719b7bff73fe9fed753ddc20ba23d8e7fdf4adfdbefadbb6a6775f7ef7eddffdfffeead7be0b38dcefeeb6afffef3d272d1b0492e733fff15dc3bfa2bfb83b9fefbfdf853fbddfbdbdf354868fd6dedf93edffca29130013bfcfbe27f4feffc86bbaa925bffdeed3fede76b321dc0abb57fe367df5adaaf30cc615c1efef7fbffe3993e583ff3721bdfbe66edef8faef24697f311ff6ff57ffefbebff9b90325bda76f77daeabfbcb9abd45c0bffe576bc3fffffc96911d477ddbbc3feef7f63a4510ec1265e6e1fe765eaafbca10400876bff7bffdfdffcc9920f60119beedfffd57e6ff383e6c3637def9fdffb7bfffb3339f94eb3fdf5bd7bbdfdf621d8f008dad195dffd6ffbff57a1ce166e5ef9f85febdde28a4a013987bf7ffebffffb56cf7aa522589bdafdf51ff4f39ed386097667fafdbfffff7ef9379dbc136bedfb9ff7aefffc3f081be97bf4e7ecfbde35cea3018d1bf1bffbfaeebefb9fac072f05bac77f7fdffeffe2eb1bd4d90a6fddafd7c2ff7bf9ba80d6f6df77ce727ff9a97fb41f03dcfbc557b3fbcc80b,
                         bigint)

    def test_version_1_noisemap(self):
        versioned_seed = RevealerPlugin.get_versioned_seed_from_user_input('125Df05b7ccf079ce2978Ae18e99219868cd')
        noise_map = RevealerPlugin.get_noise_map(versioned_seed)
        bigint = 0
        for (x, y), pixel in noise_map.items():
            if pixel:
                bigint |= 1 << (y*RevealerPlugin.SIZE[1]+x)
        self.assertEqual(0x36fde1eece10b3f674227ea76f7ababbcbf87dfba1eddf2edebfeefec3dffff719ee1cbd477b9be7cf6fcdaff924ff05a26ff2fb7bfdbbdef1a2f90c097d7cdadfbb9d1ef592c27c85efffffff7ffc8dff60d6de87f71c9fe77f7f5372cfdb1dc0eb9e959dbed42197c7ee4288f7fbf73b65fdfbd5e153ede49bb957edaefe6f7dee4a72502eef77babfa7fff7d0a3fc6f5ffefb3b7b67aab66118a56eb1fffe1ddafbeefefa96b26d715bb8e5fafbbb2ffcf64e8df2bdffeffed39ffdfdef986491a7fbf97bffb7fafee072640b7af6edf8da2f7cdff268ccd52b75f53f9afef77b4be4db9c5f9debffeff5f7f1f7b1882cb4eed67f757b37ebf0b2c7f849bd73f4737f3ffb5a3f75ac537ff5fff8edcdfeb6be63d3147ffeefa9caf7ebf740989520c1eddedabdfd73f7f821fc3977fdfbe9fbee7d6e8ca9f16b8b8f1decbffef17f806ade988d77fef5775cff3f7bd9759675f4773fff6fefaff385fe807fdbfcbbffefa6d7c4ed54a0d1959cefeecffdffe8cd539451dfdfbff71ff7e97cf37aec8069efffcf7536ebbc515e991cf293ff97feffd72cebe110d44bf787f1efecda7306ac88cd49dfff257cbd9ff7ff8fd1686eedf2dfeb373fbe2a10ed81f7d9c979316efceeea745926377ffcffba7edf67fc79cace0eeef5ff5ceffeeeff94d20c4dadd53efee6f97bfed2f8ae059ff7ffbfedfbf17f2d45bc8afdebf1dff7856ebd02c39ae22ef7befc9e97cbb7f31af5bd57e3feffafc4d7fef9ae222e9fdcf5a2dfbffefd50399d7d095d22fd7bf9fdef6d5d5044bafffdfd57fff7cbe6af91096b3f5fffe3fff7fb97fa930d316db6dfbf236ddbc8abb3bbea6edf9deafd39b8efac7ae014e7ffbdd97cfebe7ec84a72a7b323fe77afffd7f1c8eaec48e6ff3fdf7da9fffaf2d57e961d7f5debc9afe7ff32d72ff374d3ff57fff2fbffdbe9833405fcbabff8beb8ff1e55f53b2d6e96bdf7e7fbfd0fb6b130071c13cf5de5be5ef8ade46a2dd53d77ff69eff7ff946ad4e32febddff87b73fceeaf2ce94adafbb9fddeff8fbf11f4161ad6cb29dbe5f2ffe6ee2023ceeb79c76d7fff7bbffaf4485b6f6f3b7f97f9f75ce372c173177fedd65e5fb76fdc5bbf7a737f9bdddefefff1f7a5533dd1efde7ffafabcd96e1193e3cadb93e76fcdfdb4fa533bc3d3a7eff5eebc9f3ffce91aa51bbf5e7f6bcfd7dfbfd1928c0726f3f26ef8f3ffe2eb8843cbb1dfd2eabfe4f7ffec47a95263e5c65737affe73e3e3735d61e8cbffdbf75e37fc04a991ad7ff7feffa6fafdfed988b50fdf379ffdfff2f7eeb6738c0ceffff77f32fe7f2b22c866514db75f7c3df6e5fd210a70bb4bbf31bcfb6d325f4a00b06ed7d34c9dbbdffff3fd6fd8ed570d7def1dcf789ff5ae040339ff35deb5e37bedf889d83bcf5feffb77e57ffcfdd8edfd91bb8bffd3b7dbd8fea3083734c3d7dedd9ffefcb78c5d87e1919f5655bf5bf1bfb3dd65fb64ee2fffd777afef18965d03872d73bbfb6fa7df7250f3e8d6ef7ff9ffffeadff5e39abf8727fde93febddfffee3096ca1779ceabbf7ff7bda2f756353be9dfabf2bcff6feec1cad233fffbf9ecefffffa21b7b8b17ffded7ff7fef56ee44b02d9bdf3d3cf42aa777fd90ba9b08af4cfd5b797dadb3694bf3282abcb39fb2d760f9,
                         bigint)

    def test_version_1_noisemap_indexerror(self):
        versioned_seed = RevealerPlugin.get_versioned_seed_from_user_input('1A082CBDC627FFA37ABD154A64AD2565D725')
        noise_map = RevealerPlugin.get_noise_map(versioned_seed)
        bigint = 0
        for (x, y), pixel in noise_map.items():
            if pixel:
                bigint |= 1 << (y*RevealerPlugin.SIZE[1]+x)
        self.assertEqual(0x20bdba94d80b604107d92e4bb77fbdff66cbd769d14d31cc26fdbb77fffff237db49c1cb6bf5cfd4fbb7e169dfc0213b57ffbf7e7fb3dffbdce1f92bbb595efffbefeeb06e00cd6fbfcf5572e6d4f376843fed920475dfdad7dbfffedf1f5fb9de7f67ff77aefefb753daebce8eeb77ff7e35eaeefaf48fe37c7fd71ecfa96faf6d49bd1b60e29cbff7ff2f5fe7daa83d231efdfdfc2ffd17887d9aa79b1713f16dfcf75f7fa1e64c574b7abbea7abfff9c0e27b9f55cbdedffbff3eff95508796eb8bbf9dfffc367f9b6b1b59337ffebf3ff9fecdffd61a6febbc3aafff379dbafcfc814c56bfaffdd1fb7ffeb35a1c293e9f393e35b5d70fbeca50020427db9ecabaf3fff9a2211ee279fdffb53973fbbefa0d2d9270fe2fef5ffbaffefd753cc251ebff7ff352e3f77fdd50bd3975ee3ffcdff6f5fe199284436d7adfbffbbfaf9efabde086fe79bfdf21fb7efba8079b7eae57ffbabff97b3e7463300e53ff5fd5f295ffe7340062f84f689dadfd3ff13feaef33d83ef7fa9aea65fff1f53021f5baef9ffddfbfbf5dff0ad38328f03ebfadfcffdffdc45e2a9a1ef64fbe4f1b7f7fb567039baafffdffed87f7bb8784f28e7dffd7d7fbfff2e7c0d13cf0d7ff77baffefbf73f6fe851607ef9fb5bf7fd5e8fe0d07d6e9bf7de7effd3b7cbd8e55336e7fef8fcbc67fb9a74ba6481d7dfdc6f3fedd3ffe87e7184216dcffd7dfef7b7a6024b2c4d5ffc72d99d7cd5ff6da6717ecf2ffffceffb6e686a4fb4d57fbcebf7ef9b3ae4c5a553340bafff7f7377bffbe3dae1fb43b738ac7ebd5dfed0c8537fe4b0ddc277b7ffbeff63c618bebcdffe9bdff6f9e52be359a5feac691ffbcdf6abb62102b09fa66f9ffafd4b7f73d88a81e3ff2be4b7f7feba2a2566203f7af53ef7253ebf64ac799ff9e7dcff7fadadbffd23fc9b2fd9efecaeaffcff04efa1e0866fe1f9379ffaed4b9792af1b63fffceed58fcff21bac450bb7ffd9aebeffef5d6525510a55b5ffffef78f7bfa1c94ff7f3d7fcbe3df7d3fbc5a0f710157befdeff762edf2bcfed7fb7ef96ff17dd6bddb9dcf01126dfee1f5b33bf1ef3c4c21c13ffbfbfd985fbfd3804539d95ba5def9dfcdceb7b17c6bf29df6dbefbe7fb9fd9f4fd39a8fb4727b87ee579d88721c9bb3f7ffffb7ffd9df369daca81d57d5ffd0bfdeffaf1434ffcb5b6af7f7eddebdbe403b7d4abfec6f719f6b9fee205da43d79fdef7c7dbfdef2f0f61b98fb39efb43cf7eeee082d36101abb73d9effbbf77dc474f6f47fbbebb1f36b76df0dffa846efedbb7affdfbf77222153dff7fdd7dffff5e81f3b5a8ee07ff3bdfe9b77ef1fecabd51c4ef272feffebeefea7334e38d7fc5effce7ffaccffdd18506bee13bffddefbd4f092fbf6e57dddfbfd7fefdf78303790e7b1befc77f6bbcbf9348c44b37fbee7feebffb57217373b0febef97effeb29ff79daad6df17f7fedfde7eeff727c6b54217fcfbb56ffeeffbc492064ad04cff6ff9b7c2efe308364110873875bff4bb73f5c2666500afbdbbc75ff9bebc5be4465eafbbffb7ff7b7fdc8bb7dee0747df7fcfd76a4bfe5e698aa3f37fe2bffbffb65b780150337efb7a21fdfb747d14fd95ceefd7f7cfe0f6db3c0ca5eb52fb7fe82ff7f7acdea3f9ddabf48ceec4ce41bb13,
                         bigint)

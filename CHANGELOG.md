<!-- insertion marker -->
<a name="v0.6.0"></a>

## [v0.6.0](https://github.com/pity7736/nyoibo/compare/v0.5.0...v0.6.0) (2023-11-01)

### Features

- set model in field to improve error messages ([d5a5280](https://github.com/pity7736/nyoibo/commit/d5a5280305f729b373b6acfedf4bbd2f2a21d9f1))
- add formats param to date and datetime fields ([6a74289](https://github.com/pity7736/nyoibo/commit/6a74289b4f5304d7305af3181f4ec0274761c839))
- improve required error message with field name ([b25edde](https://github.com/pity7736/nyoibo/commit/b25eddea926740280f3aed921902e459fdd49f22))
- create a reverse relationship with `TupleField` ([72eb582](https://github.com/pity7736/nyoibo/commit/72eb582d812e8083fe7283d93c83f4b09bd07aa9))
- instance `Entity` from dict with tuple field ([ea73553](https://github.com/pity7736/nyoibo/commit/ea735539736b8ea4a9ee49e2ce75eddf2e987dca))

### Bug Fixes

- instance model with none value in list field with rever relationship ([442ed26](https://github.com/pity7736/nyoibo/commit/442ed26e47fe6d80891d0c479b8f9e89ea79005c))

### Docs

- upgrade requirements and readthedocs build config ([fdf19cd](https://github.com/pity7736/nyoibo/commit/fdf19cdffbd82294c115d5aebc6a1c94a2497a7b))
- upgrade python version in readthedocs config ([0268ef3](https://github.com/pity7736/nyoibo/commit/0268ef35ad2f91d7f736f64e156602ecf10c5071))

<a name="v0.5.0"></a>

## [v0.5.0](https://github.com/pity7736/nyoibo/compare/v0.4.1...v0.5.0) (2023-05-26)

### Features

- add `of` param to `TupleField` and make `ListField` a `TupleField` subclass ([4eb39c7](https://github.com/pity7736/nyoibo/commit/4eb39c75db5cfbeee6cb7fd5cd502eb5ce3e3491))
- removed `_valid_values` attribute from `LinkField` ([b7f59e7](https://github.com/pity7736/nyoibo/commit/b7f59e7cd05b318bc718939d47ad194e554f1031))
- inherit parent fields ([68a64f0](https://github.com/pity7736/nyoibo/commit/68a64f08de636c60624c35d8b2795a125cfbda70))
- add alias param to fields ([d07a3b9](https://github.com/pity7736/nyoibo/commit/d07a3b93564e74530a25d1b9d59f44e6c2ccd663))

### Bug Fixes

- required LinkField ([1b7ae5c](https://github.com/pity7736/nyoibo/commit/1b7ae5c591b63243eca60b6ab1be3520ec153eba))

### Build

- fix tests requires ([ff5460b](https://github.com/pity7736/nyoibo/commit/ff5460bedd4f8834f0cb98ab91f683c206f8341a))

### Chore

- make python3.9 as a minimum version ([6ddabc1](https://github.com/pity7736/nyoibo/commit/6ddabc14a8503b90c8580ada51816fb301b45b69))

### Continuous Integration

- drop python 3.7 and 4.8 support. add python3.11 ([7a231e2](https://github.com/pity7736/nyoibo/commit/7a231e2c4bc49def317242fdac2a4d0f64135226))

### Dependencies

- update dev dependencies ([41b6b6c](https://github.com/pity7736/nyoibo/commit/41b6b6c78f5f5a56a84174f307b3c0f20269a185))

<a name="v0.4.1"></a>

## [v0.4.1](https://github.com/pity7736/nyoibo/compare/v0.4.0...v0.4.1) (2022-03-02)

### Docs

- **fix:** update usage examples ([552b84b](https://github.com/pity7736/nyoibo/commit/552b84b7009da138cddfda7048efe5b9229dd0a0))
- **fix:** readme ([740fee8](https://github.com/pity7736/nyoibo/commit/740fee8e76fc27e5b31a0c996fa951db9b611f2e))

<a name="v0.4.0"></a>

## [v0.4.0](https://github.com/pity7736/nyoibo/compare/v0.3.0...v0.4.0) (2022-02-25)

### Features

- add `ListField` ([8c2616b](https://github.com/pity7736/nyoibo/commit/8c2616b8fac10a789ad7542722d9b3aa5d30180a))
- add `TupleField` ([f4f6c65](https://github.com/pity7736/nyoibo/commit/f4f6c65ddf9a7d5267994668fd70decc839e64eb))
- **fields:** add `JSONField` ([95eb1b0](https://github.com/pity7736/nyoibo/commit/95eb1b0e22789480719bf52d1267d528c7ccec7f))
- add `min_value` and `max_value` to `IntField` ([ca610b8](https://github.com/pity7736/nyoibo/commit/ca610b8be374aa237fdc916c6e73cf3e61d2daca))
- add `max_length` param to `StrField` ([8ab928a](https://github.com/pity7736/nyoibo/commit/8ab928a74b5f1b50138aa8c0a3644cfb0f713ec0))
- add `mutable` param to field ([5278cb8](https://github.com/pity7736/nyoibo/commit/5278cb8970265bf9e3a42218985519e7acf689d3))
- add required param to field ([69f7eaf](https://github.com/pity7736/nyoibo/commit/69f7eafc3e781f931cbd46c0c1229ec07d7d5636))

### Docs

- update field docstrings ([0b82861](https://github.com/pity7736/nyoibo/commit/0b8286129ee85a7d2982cc68715aa9f10b259820))

<a name="v0.3.0"></a>

## [v0.3.0](https://github.com/pity7736/nyoibo/compare/v0.2.1...v0.3.0) (2022-01-25)

### Features

- **fields:** add DictField ([6ccc132](https://github.com/pity7736/nyoibo/commit/6ccc132e5ff9ec5ab01d2e0f34cd4733bbe04158))
- parse LinkField from dict ([8809589](https://github.com/pity7736/nyoibo/commit/8809589e5d961539ef9faede8dcd16f0b0dedc2f))

### Bug Fixes

- **ci:** add python3.10 job to jobs ([99ef290](https://github.com/pity7736/nyoibo/commit/99ef2902018f95e2cb7990e0930d18b4116c531a))

### Build

- version 0.3.0 ([cb6cc2c](https://github.com/pity7736/nyoibo/commit/cb6cc2c39a653248cececb2331917339b2cd2dc1))

### Chore

- update requirements for python3.10 support ([e9f7d57](https://github.com/pity7736/nyoibo/commit/e9f7d573797a56ca0032a156a0f42b0e6175a73e))
- **changelog:** use git-autochangelog ([a7cefd9](https://github.com/pity7736/nyoibo/commit/a7cefd94ecec0cefa94b250c0743596c79fbd769))

### Continuous Integration

- test on python 3.10 ([211c408](https://github.com/pity7736/nyoibo/commit/211c4089ec12d628e9341834acfb2e2798610d37))

<a name="v0.2.1"></a>

## [v0.2.1](https://github.com/pity7736/nyoibo/compare/v0.2.0...v0.2.1) (2021-03-28)

### Features

- validate if value of internal type ([508f8c9](https://github.com/pity7736/nyoibo/commit/508f8c9df3d17b597df73cb75f71dca9d01461ed))
- set value to immutable field from another field. ([2e22662](https://github.com/pity7736/nyoibo/commit/2e22662988726f357f198490fed3661d86813e28))

### Build

- version 0.2.1 ([fd9501b](https://github.com/pity7736/nyoibo/commit/fd9501b178c0a8d95cff2503aa5ae6838bbc90a9))

### Chore

- added commit to changelog ([2f4544c](https://github.com/pity7736/nyoibo/commit/2f4544c97f2bcf699a1eec851d51239f65e18b5f))
- created changelog file ([f66ccfc](https://github.com/pity7736/nyoibo/commit/f66ccfcc305e57162529d07126418fb9f58e04ef))

<a name="v0.2.0"></a>

## [v0.2.0](https://github.com/pity7736/nyoibo/compare/v0.1.0...v0.2.0) (2021-02-09)

### Features

- add extra behvaior by inheritance ([6e1580c](https://github.com/pity7736/nyoibo/commit/6e1580cf1be892d8d601e1985255be563a5a2292))
- `to` param on LinkField could be an Entity with another metaclass ([db64857](https://github.com/pity7736/nyoibo/commit/db64857a494f250e0b7ec966796fa5d458cc3e89))
- to in LinkField could be a MetaEntity subclass ([8261406](https://github.com/pity7736/nyoibo/commit/82614069065bdd3f5e314c7d6ecc81055b66c239))

### Bug Fixes

- value to LinkField can by None ([c4648a8](https://github.com/pity7736/nyoibo/commit/c4648a815a9ca2f362ca34ba037211e465c9a1d3))

### Chore

- changed license from GPLv3 to LGPLv3 ([a9fad8f](https://github.com/pity7736/nyoibo/commit/a9fad8fa4e3a4154a8e9538e1074a59709e7edd5))
- set python 3.7 as minimun version ([ec45ce2](https://github.com/pity7736/nyoibo/commit/ec45ce2bbda95015a524ce427986def02076cce1))

### Continuous Integration

- test with python 3.9 ([4ebb682](https://github.com/pity7736/nyoibo/commit/4ebb6820db07cc4c88fb49a1145a5fc7caabc843))

### Docs

- install doc ([59be579](https://github.com/pity7736/nyoibo/commit/59be5794e0019e6ca42c24c88ff912cabaf9c61f))

<a name="v0.1.0"></a>

## [v0.1.0](https://github.com/pity7736/nyoibo/compare/a508d591c389e7dd2e0a8afda71160e7d7a693d6...v0.1.0) (2020-07-24)

### Features

- validate to type in LinkField ([34c0be3](https://github.com/pity7736/nyoibo/commit/34c0be35ab16fa451c864d13cfd34207c59665a4))
- raise exception to missing fields ([c63f0f1](https://github.com/pity7736/nyoibo/commit/c63f0f1457810eec9def693f2bfa581e6222aa1a))
- raise date value exception when value is wrong type ([0643f2c](https://github.com/pity7736/nyoibo/commit/0643f2ccdf9a2e1dd93e2003d5b537c34700448e))
- raise exception when value is wrong type ([93e5f0c](https://github.com/pity7736/nyoibo/commit/93e5f0c705bf197877183311e6265afa7b06d006))
- added choices param to field ([fcaeb39](https://github.com/pity7736/nyoibo/commit/fcaeb399d9aecbc840c62fbaf3c7b6b46541a4b8))
- made fields public by default ([24ae047](https://github.com/pity7736/nyoibo/commit/24ae04799a776cf7024ce2b09e9429834794a0be))
- fields are private and immutable by default ([47f0469](https://github.com/pity7736/nyoibo/commit/47f0469dfdba0dce823aacf9b513f285a28a992d))
- add entity field ([ec726b2](https://github.com/pity7736/nyoibo/commit/ec726b28aebbd3c645ab77b374c146c77a5db50b))
- override getter/setter ([b8ac39b](https://github.com/pity7736/nyoibo/commit/b8ac39b7abcded3884963b596707fb2451b92733))
- add immutable param to Fields ([661e260](https://github.com/pity7736/nyoibo/commit/661e2605bc25653eccf9ac5bfb1cbd024c6c0af5))
- add private param to Field. ([da311b0](https://github.com/pity7736/nyoibo/commit/da311b0b5e8e29cfdbbc6bf43469124d8645c090))
- add default_value param in Fields ([647945e](https://github.com/pity7736/nyoibo/commit/647945ebd6bb4a707f7feb4e5387f9a0fe8fdd6e))
- add Float and Decimal fields ([5ed918a](https://github.com/pity7736/nyoibo/commit/5ed918aa33930f56577021b22a9cebedbf8ed1e6))
- add Date and Datetime fields ([1566193](https://github.com/pity7736/nyoibo/commit/156619304b18500d916e0190d8a9a140bae5ab86))
- add BooleanField ([a9d2b03](https://github.com/pity7736/nyoibo/commit/a9d2b03d47f85151f4f3dbc015a6b9ce0c7bbc51))
- parse string floats to int ([228a9cd](https://github.com/pity7736/nyoibo/commit/228a9cdd8b31e20c987b80092cf873e5ab86784c))
- add IntField ([f5601dc](https://github.com/pity7736/nyoibo/commit/f5601dca674df2eaeecc5066f0ae034fd56d43bc))
- value setter ([23d74ca](https://github.com/pity7736/nyoibo/commit/23d74caa4ac880b1f42c666aba0a86939fea084b))
- private fields validations ([87ac7e3](https://github.com/pity7736/nyoibo/commit/87ac7e378ce7ca7ecde169ae663a23cf633a948f))

### Bug Fixes

- assign value to private field ([df721b0](https://github.com/pity7736/nyoibo/commit/df721b0d370443e21d4093217532a963fa3ece14))

### Code Refactoring

- the validation was pushed up to Field ([cc4da97](https://github.com/pity7736/nyoibo/commit/cc4da977c75dbf0e7a86e010a6b6f14fa168ddc1))
- renamed EntityField to LinkField ([33d8705](https://github.com/pity7736/nyoibo/commit/33d870527d313b552aafefa3cb8c9ccf5d8eb43f))
- rename value param to field ([b062bee](https://github.com/pity7736/nyoibo/commit/b062bee2d1ed7cac8519e2b7652d7ef5990d2043))
- remove fields param ([42a73a6](https://github.com/pity7736/nyoibo/commit/42a73a6919cb9ae23ac7fb0bda50d0f500aa1aca))
- removed unnecessary interfaces ([1d559c3](https://github.com/pity7736/nyoibo/commit/1d559c3fbafd0422c596cd9d3ba02a645b925aad))
- dynamically nitialize fields ([2c486f3](https://github.com/pity7736/nyoibo/commit/2c486f3d54a04e636f7cfeb0c5caaf15b7712899))
- getters and setters ([e5ca277](https://github.com/pity7736/nyoibo/commit/e5ca27762cde180663b13093ca808a6ab749ef98))

### Tests

- override setter parsing value ([b1b8b35](https://github.com/pity7736/nyoibo/commit/b1b8b355dba3c243f1b91fc5afa1e4f1e320d86b))
- changed test_fields approach ([b6bc39c](https://github.com/pity7736/nyoibo/commit/b6bc39ceca9dea26b4ba2cd37c2899a03a736398))
- add more cases ([0c21a3d](https://github.com/pity7736/nyoibo/commit/0c21a3d38be22a7e01b1db21b91ca1531bea4e8b))
- get uninitialized values ([d301bc9](https://github.com/pity7736/nyoibo/commit/d301bc90a09d5a93d1ce316262f59b847d2f9572))
- first skeleton ([cdc848b](https://github.com/pity7736/nyoibo/commit/cdc848bf1a1994c4b99953774a94e42925f1067b))

### Chore

- resize image ([3f25675](https://github.com/pity7736/nyoibo/commit/3f256753a2ec5ce03b277ec2e10caf5af66bf885))
- second try to resize noyibo image ([b252e08](https://github.com/pity7736/nyoibo/commit/b252e0871d59123a80aa093dea3263fcb6eb6ad6))
- resized nyoibo image ([508634c](https://github.com/pity7736/nyoibo/commit/508634ce37afc7604fd1d1bcfa7864533de743f0))
- added cython to requirements ([f7f31fe](https://github.com/pity7736/nyoibo/commit/f7f31fe2a72fbcffa7a5022359fc3856806c8565))
- use list instead tuple extensions ([74489a4](https://github.com/pity7736/nyoibo/commit/74489a489dcbd1b9602fc1c34d09da0b7b117b77))
- no required cython to install nyoibo ([6db0254](https://github.com/pity7736/nyoibo/commit/6db025483650f99ce896b4ab7e5938e53b4ff076))
- replace radon with xenon ([add067c](https://github.com/pity7736/nyoibo/commit/add067c976fd5934fd71b83a705f8eac57b13878))
- exclude c files in trailing-whitespace hook ([8e0415b](https://github.com/pity7736/nyoibo/commit/8e0415b71f84fdea063beed0e1c12a923d0ee379))
- missing things from python template ([798bb87](https://github.com/pity7736/nyoibo/commit/798bb87f9d1ce70b9813bcfeb64fa6d79ad1c2c0))

### Continuous Integration

- skip python 3.6 tests ([2d179fa](https://github.com/pity7736/nyoibo/commit/2d179faa17ea504072ff63636cad9e2203957407))
- renamed ci config file ([6b6bb2f](https://github.com/pity7736/nyoibo/commit/6b6bb2f7dd132d4d0f105c30d384172d99fa9519))
- renamed ci directory ([56a499b](https://github.com/pity7736/nyoibo/commit/56a499b484895f5ec38b0d055f46e33ee3c1cc38))
- circle configuration ([ceb5f8b](https://github.com/pity7736/nyoibo/commit/ceb5f8b8e7543614f96734ef38f6995dfd9fd6b0))

### Docs

- updated LinkField ([921ebd3](https://github.com/pity7736/nyoibo/commit/921ebd375ec3eb1ab5aa04a12e17fe3ac29de362))
- add members to entity doc ([c45f8db](https://github.com/pity7736/nyoibo/commit/c45f8dbd3098899ab478d8fa72c315094dab65bd))
- ... ([e6bddb2](https://github.com/pity7736/nyoibo/commit/e6bddb24d0594ea308e6638f2f804761fe6e98ea))
- added cython to requirements ([7f775ea](https://github.com/pity7736/nyoibo/commit/7f775ea169387b153a722a676ad8272ffdd024fe))
- install with pip locally ([f84218d](https://github.com/pity7736/nyoibo/commit/f84218ddc6f15adf667bc1f02f7cb957a25006c3))
- install nyoibo via setuptools ([f072ff2](https://github.com/pity7736/nyoibo/commit/f072ff26f9e46d1ba711c5ab7c3241ebf219e827))
- added local project to doc requirements ([8a20390](https://github.com/pity7736/nyoibo/commit/8a20390248389388d561ca7851dec72fb40c1ec6))
- api reference ([efdc5fa](https://github.com/pity7736/nyoibo/commit/efdc5faff21054cb1f4ca09e995cea6c9d77251c))
- fix typo ([4c79d1c](https://github.com/pity7736/nyoibo/commit/4c79d1c0c006e52ef8c3278e32e0da54efbd9534))
- usage ([0edd2e7](https://github.com/pity7736/nyoibo/commit/0edd2e722016fa5d2d1059e85a7be83e5251fe57))
- added the nyoibo meaning ([4740697](https://github.com/pity7736/nyoibo/commit/4740697b29c52ba007dfa15f25d0942ee6be8859))
- readme fixes ([c24979a](https://github.com/pity7736/nyoibo/commit/c24979ad8d8546bb966f6ddf7739ad04b3920668))
- fix example dataclass code ([534f502](https://github.com/pity7736/nyoibo/commit/534f502d836f7287a615d2633954043c5ea4f828))
- readme improvements ([d4cdc18](https://github.com/pity7736/nyoibo/commit/d4cdc181e7a1bff2bf0d0ac83ae27abc6b7d39e2))
- rst improvements ([7612747](https://github.com/pity7736/nyoibo/commit/7612747bf6423bf43d61600c7d609d4804f20fd7))
- updated readme ([20585f0](https://github.com/pity7736/nyoibo/commit/20585f09d229d3f572d27360eca19beeeca47f04))
- fix doc url ([1d04447](https://github.com/pity7736/nyoibo/commit/1d04447a895d4949c734f5a39b711c01afc54079))
- init configuration ([5dc4fd3](https://github.com/pity7736/nyoibo/commit/5dc4fd309ed15990905f442adb091b332151d550))

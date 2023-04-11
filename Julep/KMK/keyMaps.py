from kmk.keys import KC

kcToCharDict = {}


# TODO: Figure out how to get TRNS stuff converted... i might need to pass in something in addition to keycode
def convertKCtoChar(keycode):
    if keycode not in kcToCharDict or len(kcToCharDict[keycode]) != 1:
        return " "
    else:
        return kcToCharDict[keycode]


def createLayerTap(keycode, layer):
    return KC.LT(layer, keycode, prefer_hold=True, tap_interrupted=True, tap_time=200)


def createModTap(tap, hold):
    return KC.MT(tap, hold, prefer_hold=True, tap_interrupted=True, tap_time=200)


def getKeymap():
    # I get these characters from here: https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_cga
    standardKCStrings = {
        KC.NO: " ",
        KC.TRNS: " ",
        KC.A: "A",
        KC.B: "B",
        KC.C: "C",
        KC.D: "D",
        KC.E: "E",
        KC.F: "F",
        KC.G: "G",
        KC.H: "H",
        KC.I: "I",
        KC.J: "J",
        KC.K: "K",
        KC.L: "L",
        KC.M: "M",
        KC.N: "N",
        KC.O: "O",
        KC.P: "P",
        KC.Q: "Q",
        KC.R: "R",
        KC.S: "S",
        KC.T: "T",
        KC.U: "U",
        KC.V: "V",
        KC.W: "W",
        KC.X: "X",
        KC.Y: "Y",
        KC.Z: "Z",
        KC.N1: "1",
        KC.N2: "2",
        KC.N3: "3",
        KC.N4: "4",
        KC.N5: "5",
        KC.N6: "6",
        KC.N7: "7",
        KC.N8: "8",
        KC.N9: "9",
        KC.N0: "0",
        KC.ENT: "↕",
        KC.ESC: "e",
        KC.BSPC: "◄",
        KC.TAB: "↔",
        KC.SPC: "‿",
        KC.MINS: "-",
        KC.EQL: "=",
        KC.LBRC: "[",
        KC.RBRC: "]",
        KC.BSLS: "\\",
        KC.SCLN: ";",
        KC.QUOT: "'",
        KC.GRV: "`",
        KC.COMM: ",",
        KC.DOT: ".",
        KC.SLSH: "/",
        KC.CAPS: " ",
        KC.F1: "1",
        KC.F2: "2",
        KC.F3: "3",
        KC.F4: "4",
        KC.F5: "5",
        KC.F6: "6",
        KC.F7: "7",
        KC.F8: "8",
        KC.F9: "9",
        KC.F10: "0",
        KC.F11: "₁",
        KC.F12: "₂",
        KC.RGHT: "→",
        KC.LEFT: "←",
        KC.DOWN: "↓",
        KC.UP: "↑",
        KC.F13: "F",
        KC.F14: "F",
        KC.F15: "F",
        KC.F16: "F",
        KC.F17: "F",
        KC.F18: "F",
        KC.F19: "F",
        KC.F20: "F",
        KC.F21: "F",
        KC.F22: "F",
        KC.F23: "F",
        KC.F24: "F",
        KC.LCTL: "ˆ",
        KC.RCTL: "ˆ",
        KC.LSFT: " ",
        KC.RSFT: " ",
        KC.LALT: " ",
        KC.RALT: " ",
        KC.LGUI: "☻",
        KC.RGUI: "☻",
        KC.TILD: "~",
        KC.EXLM: "!",
        KC.AT: "@",
        KC.HASH: "#",
        KC.DLR: "$",
        KC.PERC: "%",
        KC.CIRC: "^",
        KC.AMPR: "&",
        KC.ASTR: "*",
        KC.LPRN: "(",
        KC.RPRN: ")",
        KC.UNDS: "_",
        KC.PLUS: "+",
        KC.LCBR: "{",
        KC.RCBR: "}",
        KC.PIPE: "|",
        KC.COLN: ":",
        KC.DQT: '"',
        KC.LABK: "<",
        KC.RABK: ">",
        KC.QUES: "?",
        KC.MUTE: "×",
        KC.VOLU: "▲",
        KC.VOLD: "▼",
        KC.BRIU: "☼",
        KC.BRID: "☼",
        KC.MNXT: "»",
        KC.MPRV: "«",
        KC.MSTP: "█",
        KC.MPLY: "║",
        KC.EJCT: " ",
        KC.MFFD: "»",
        KC.MRWD: "«",
    }

    ZSHFT = createModTap(KC.Z, KC.LSFT)
    SLSHSHFT = createModTap(KC.SLSH, KC.RSFT)
    BSPCCMND = createModTap(KC.BSPC, KC.LGUI)
    SPCALT = createModTap(KC.SPC, KC.LALT)
    TABALT = createModTap(KC.TAB, KC.RALT)
    ENTCTRL = createModTap(KC.ENT, KC.RCTRL)
    ALAYER = createLayerTap(KC.A, 2)
    QLAYER = createLayerTap(KC.Q, 3)
    PLAYER = createLayerTap(KC.P, 3)
    SCLAYER = createLayerTap(KC.SCLN, 4)
    RGUIEMOJI = KC.TD(KC.RGUI, KC.RCTRL(KC.RGUI(KC.SPC)))
    CTRLWINMV = KC.TD(KC.LCTRL, KC.LCTRL(KC.LALT))

    MACSCREENSHOT = KC.LGUI(KC.LSFT(KC.N4))
    customKCStrings = {
        ZSHFT: standardKCStrings[KC.Z],
        SLSHSHFT: standardKCStrings[KC.SLSH],
        BSPCCMND: standardKCStrings[KC.BSPC],
        MACSCREENSHOT: "┼",
        ALAYER: standardKCStrings[KC.A],
        QLAYER: standardKCStrings[KC.Q],
        PLAYER: standardKCStrings[KC.P],
        SCLAYER: standardKCStrings[KC.SCLN],
        SPCALT: standardKCStrings[KC.SPC],
        TABALT: standardKCStrings[KC.TAB],
        ENTCTRL: standardKCStrings[KC.ENT],
        RGUIEMOJI: standardKCStrings[KC.RGUI],
        CTRLWINMV: standardKCStrings[KC.LCTRL],
    }

    kcToCharDict.update(customKCStrings)
    kcToCharDict.update(standardKCStrings)

    # fmt: off
    return [
        # Base Layer 1 - Querty
        [
            QLAYER,     KC.W,       KC.E,       KC.R,       KC.T,       KC.Y,       KC.U,       KC.I,       KC.O,   PLAYER,
            ALAYER,     KC.S,       KC.D,       KC.F,       KC.G,       KC.H,       KC.J,       KC.K,       KC.L,   SCLAYER,
            ZSHFT,      KC.X,       KC.C,       KC.V,       KC.B,       KC.N,       KC.M,       KC.COMM,    KC.DOT, SLSHSHFT,
            KC.NO,      KC.NO,      CTRLWINMV,  SPCALT,     BSPCCMND,   RGUIEMOJI,  TABALT,     ENTCTRL,    KC.NO,  KC.NO   
        ],
        # Base Layer 2 - Colemak DH - Currently not used by code. This layer is essentially ignored
        [
            KC.TRNS,    KC.TRNS,    KC.F,       KC.P,       KC.B,       KC.J,       KC.L,       KC.U,       KC.Y,       KC.SCLN,
            KC.TRNS,    KC.R,       KC.S,       KC.T,       KC.TRNS,    KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.D,       KC.V,       KC.K,       KC.H,       KC.TRNS,    KC.TRNS,    KC.TRNS,
            KC.NO,      KC.NO,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.NO,      KC.NO
        ],
        # Symbol Layer
        [
            KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,    KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,
            KC.NO,      KC.UNDS,    KC.PIPE,    KC.GRV,     KC.QUOT,    KC.DQT,     KC.NO,      KC.NO,      KC.LBRC,    KC.RBRC,
            KC.NO,      KC.NO,      KC.NO,      KC.TILDE,   KC.NO,      KC.NO,      KC.LABK,    KC.RABK,    KC.LCBR,    KC.RCBR,
            KC.NO,      KC.NO,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.NO,      KC.NO
        ],
        # Number/Arrow Layer
        [
            KC.NO,      KC.NO,      KC.UP,      KC.NO,      KC.NO,      KC.PLUS,    KC.N7,      KC.N8,      KC.N9,  KC.ASTR,
            KC.NO,      KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.NO,      KC.MINS,    KC.N4,      KC.N5,      KC.N6,  KC.BSLS,
            KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.N0,      KC.N1,      KC.N2,      KC.N3,  KC.EQL,
            KC.NO,      KC.NO,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.NO,  KC.NO
        ],
        # Function/System Layer
        [
            KC.ESC, MACSCREENSHOT,  KC.MUTE,    KC.VOLD,    KC.VOLU,        KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.NO,
            KC.CAPS,        KC.NO,  KC.MPRV,    KC.MPLY,    KC.MNXT,        KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.NO,
            KC.NO,          KC.NO,  KC.NO,      KC.BRID,    KC.BRIU,        KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.NO,
            KC.NO,          KC.NO,  KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.NO,      KC.NO
        ]
    ]
    # fmt: on

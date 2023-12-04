pub fn run(inp: &str) -> i64 {
    let mut res = 0;

    unsafe {
        for line in inp.lines() {
            let mut owned: [bool; 100] = [false; 100];

            for i in 0..10 {
                // we take index 10 + i*3 and that +1 to parse as usize
                // space is equal to 0

                let mut val = 0;
                let first_char = line.as_bytes().get_unchecked(10 + i * 3);
                if *first_char != b' ' {
                    val = (first_char - b'0') * 10;
                }
                let second_char = line.as_bytes().get_unchecked(10 + i * 3 + 1);
                val += second_char - b'0';

                *owned.get_unchecked_mut(val as usize) = true;
            }

            let mut card_val = 1;

            for j in 0..25 {
                let mut val = 0;
                let first_char = line.as_bytes().get_unchecked(42 + j * 3);
                if *first_char != b' ' {
                    val = (first_char - b'0') * 10;
                }
                let second_char = line.as_bytes().get_unchecked(42 + j * 3 + 1);
                val += second_char - b'0';

                if *owned.get_unchecked(val as usize) {
                    card_val *= 2;
                }
            }

            if card_val > 1 {
                res += card_val / 2;
            }
        }
    }
    res
}

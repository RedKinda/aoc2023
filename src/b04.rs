pub fn run(inp: &str) -> i64 {
    let mut res = 0;

    let mut won_copies: [u32; 245] = [0; 245];

    unsafe {
        for (ind, line) in inp.lines().enumerate() {
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

            let mut owned_count = 0;

            for j in 0..25 {
                let mut val = 0;
                let first_char = line.as_bytes().get_unchecked(42 + j * 3);
                if *first_char != b' ' {
                    val = (first_char - b'0') * 10;
                }
                let second_char = line.as_bytes().get_unchecked(42 + j * 3 + 1);
                val += second_char - b'0';

                if *owned.get_unchecked(val as usize) {
                    owned_count += 1;
                }
            }

            let copies = 1 + *won_copies.get_unchecked(ind);

            if owned_count > 0 {
                for i in 0..=owned_count {
                    *won_copies.get_unchecked_mut(ind + i) += copies;
                }
            }

            // println!("cards: {}, copies: {}", owned_count, copies);

            res += copies as i64;
        }
    }

    res
}

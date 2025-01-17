// Do not edit - auto-generated
module apb_plic_regs (
  input  logic [30:0][ 2:0] prio_i,
  output logic [30:0][ 2:0] prio_o,
  output logic [30:0]       prio_we_o,
  output logic [30:0]       prio_re_o,
  input  logic [ 0:0][30:0] ip_i,
  output logic [ 0:0]       ip_re_o,
  input  logic [ 1:0][30:0] ie_i,
  output logic [ 1:0][30:0] ie_o,
  output logic [ 1:0]       ie_we_o,
  output logic [ 1:0]       ie_re_o,
  input  logic [ 1:0][ 2:0] threshold_i,
  output logic [ 1:0][ 2:0] threshold_o,
  output logic [ 1:0]       threshold_we_o,
  output logic [ 1:0]       threshold_re_o,
  input  logic [ 1:0][ 4:0] cc_i,
  output logic [ 1:0][ 4:0] cc_o,
  output logic [ 1:0]       cc_we_o,
  output logic [ 1:0]       cc_re_o,
  // APB3 interface
  input  logic [31:0] paddr_i,
  input  logic        psel_i,
  input  logic        penable_i,
  input  logic        pwrite_i,
  input  logic [31:0] pwdata_i,
  output logic [31:0] prdata_o,
  output logic        pready_o,
  output logic        pslverr_o
);

  always_comb begin
    pready_o = 1'b1;
    prdata_o = '0;
    pslverr_o = '0;
    prio_o = '0;
    prio_we_o = '0;
    prio_re_o = '0;
    ie_o = '0;
    ie_we_o = '0;
    ie_re_o = '0;
    threshold_o = '0;
    threshold_we_o = '0;
    threshold_re_o = '0;
    cc_o = '0;
    cc_we_o = '0;
    cc_re_o = '0;
    if (psel_i & penable_i) begin
      if (pwrite_i) begin
        unique case(paddr_i)
          32'hc000000: begin
            prio_o[0][2:0] = pwdata_i[2:0];
            prio_we_o[0] = 1'b1;
          end
          32'hc000004: begin
            prio_o[1][2:0] = pwdata_i[2:0];
            prio_we_o[1] = 1'b1;
          end
          32'hc000008: begin
            prio_o[2][2:0] = pwdata_i[2:0];
            prio_we_o[2] = 1'b1;
          end
          32'hc00000c: begin
            prio_o[3][2:0] = pwdata_i[2:0];
            prio_we_o[3] = 1'b1;
          end
          32'hc000010: begin
            prio_o[4][2:0] = pwdata_i[2:0];
            prio_we_o[4] = 1'b1;
          end
          32'hc000014: begin
            prio_o[5][2:0] = pwdata_i[2:0];
            prio_we_o[5] = 1'b1;
          end
          32'hc000018: begin
            prio_o[6][2:0] = pwdata_i[2:0];
            prio_we_o[6] = 1'b1;
          end
          32'hc00001c: begin
            prio_o[7][2:0] = pwdata_i[2:0];
            prio_we_o[7] = 1'b1;
          end
          32'hc000020: begin
            prio_o[8][2:0] = pwdata_i[2:0];
            prio_we_o[8] = 1'b1;
          end
          32'hc000024: begin
            prio_o[9][2:0] = pwdata_i[2:0];
            prio_we_o[9] = 1'b1;
          end
          32'hc000028: begin
            prio_o[10][2:0] = pwdata_i[2:0];
            prio_we_o[10] = 1'b1;
          end
          32'hc00002c: begin
            prio_o[11][2:0] = pwdata_i[2:0];
            prio_we_o[11] = 1'b1;
          end
          32'hc000030: begin
            prio_o[12][2:0] = pwdata_i[2:0];
            prio_we_o[12] = 1'b1;
          end
          32'hc000034: begin
            prio_o[13][2:0] = pwdata_i[2:0];
            prio_we_o[13] = 1'b1;
          end
          32'hc000038: begin
            prio_o[14][2:0] = pwdata_i[2:0];
            prio_we_o[14] = 1'b1;
          end
          32'hc00003c: begin
            prio_o[15][2:0] = pwdata_i[2:0];
            prio_we_o[15] = 1'b1;
          end
          32'hc000040: begin
            prio_o[16][2:0] = pwdata_i[2:0];
            prio_we_o[16] = 1'b1;
          end
          32'hc000044: begin
            prio_o[17][2:0] = pwdata_i[2:0];
            prio_we_o[17] = 1'b1;
          end
          32'hc000048: begin
            prio_o[18][2:0] = pwdata_i[2:0];
            prio_we_o[18] = 1'b1;
          end
          32'hc00004c: begin
            prio_o[19][2:0] = pwdata_i[2:0];
            prio_we_o[19] = 1'b1;
          end
          32'hc000050: begin
            prio_o[20][2:0] = pwdata_i[2:0];
            prio_we_o[20] = 1'b1;
          end
          32'hc000054: begin
            prio_o[21][2:0] = pwdata_i[2:0];
            prio_we_o[21] = 1'b1;
          end
          32'hc000058: begin
            prio_o[22][2:0] = pwdata_i[2:0];
            prio_we_o[22] = 1'b1;
          end
          32'hc00005c: begin
            prio_o[23][2:0] = pwdata_i[2:0];
            prio_we_o[23] = 1'b1;
          end
          32'hc000060: begin
            prio_o[24][2:0] = pwdata_i[2:0];
            prio_we_o[24] = 1'b1;
          end
          32'hc000064: begin
            prio_o[25][2:0] = pwdata_i[2:0];
            prio_we_o[25] = 1'b1;
          end
          32'hc000068: begin
            prio_o[26][2:0] = pwdata_i[2:0];
            prio_we_o[26] = 1'b1;
          end
          32'hc00006c: begin
            prio_o[27][2:0] = pwdata_i[2:0];
            prio_we_o[27] = 1'b1;
          end
          32'hc000070: begin
            prio_o[28][2:0] = pwdata_i[2:0];
            prio_we_o[28] = 1'b1;
          end
          32'hc000074: begin
            prio_o[29][2:0] = pwdata_i[2:0];
            prio_we_o[29] = 1'b1;
          end
          32'hc000078: begin
            prio_o[30][2:0] = pwdata_i[2:0];
            prio_we_o[30] = 1'b1;
          end
          32'hc002000: begin
            ie_o[0][30:0] = pwdata_i[30:0];
            ie_we_o[0] = 1'b1;
          end
          32'hc002080: begin
            ie_o[1][30:0] = pwdata_i[30:0];
            ie_we_o[1] = 1'b1;
          end
          32'hc200000: begin
            threshold_o[0][2:0] = pwdata_i[2:0];
            threshold_we_o[0] = 1'b1;
          end
          32'hc201000: begin
            threshold_o[1][2:0] = pwdata_i[2:0];
            threshold_we_o[1] = 1'b1;
          end
          32'hc200004: begin
            cc_o[0][4:0] = pwdata_i[4:0];
            cc_we_o[0] = 1'b1;
          end
          32'hc201004: begin
            cc_o[1][4:0] = pwdata_i[4:0];
            cc_we_o[1] = 1'b1;
          end
          default: pslverr_o = 1'b1;
        endcase
      end else begin
        unique case(paddr_i)
          32'hc000000: begin
            prdata_o[2:0] = prio_i[0][2:0];
            prio_re_o[0] = 1'b1;
          end
          32'hc000004: begin
            prdata_o[2:0] = prio_i[1][2:0];
            prio_re_o[1] = 1'b1;
          end
          32'hc000008: begin
            prdata_o[2:0] = prio_i[2][2:0];
            prio_re_o[2] = 1'b1;
          end
          32'hc00000c: begin
            prdata_o[2:0] = prio_i[3][2:0];
            prio_re_o[3] = 1'b1;
          end
          32'hc000010: begin
            prdata_o[2:0] = prio_i[4][2:0];
            prio_re_o[4] = 1'b1;
          end
          32'hc000014: begin
            prdata_o[2:0] = prio_i[5][2:0];
            prio_re_o[5] = 1'b1;
          end
          32'hc000018: begin
            prdata_o[2:0] = prio_i[6][2:0];
            prio_re_o[6] = 1'b1;
          end
          32'hc00001c: begin
            prdata_o[2:0] = prio_i[7][2:0];
            prio_re_o[7] = 1'b1;
          end
          32'hc000020: begin
            prdata_o[2:0] = prio_i[8][2:0];
            prio_re_o[8] = 1'b1;
          end
          32'hc000024: begin
            prdata_o[2:0] = prio_i[9][2:0];
            prio_re_o[9] = 1'b1;
          end
          32'hc000028: begin
            prdata_o[2:0] = prio_i[10][2:0];
            prio_re_o[10] = 1'b1;
          end
          32'hc00002c: begin
            prdata_o[2:0] = prio_i[11][2:0];
            prio_re_o[11] = 1'b1;
          end
          32'hc000030: begin
            prdata_o[2:0] = prio_i[12][2:0];
            prio_re_o[12] = 1'b1;
          end
          32'hc000034: begin
            prdata_o[2:0] = prio_i[13][2:0];
            prio_re_o[13] = 1'b1;
          end
          32'hc000038: begin
            prdata_o[2:0] = prio_i[14][2:0];
            prio_re_o[14] = 1'b1;
          end
          32'hc00003c: begin
            prdata_o[2:0] = prio_i[15][2:0];
            prio_re_o[15] = 1'b1;
          end
          32'hc000040: begin
            prdata_o[2:0] = prio_i[16][2:0];
            prio_re_o[16] = 1'b1;
          end
          32'hc000044: begin
            prdata_o[2:0] = prio_i[17][2:0];
            prio_re_o[17] = 1'b1;
          end
          32'hc000048: begin
            prdata_o[2:0] = prio_i[18][2:0];
            prio_re_o[18] = 1'b1;
          end
          32'hc00004c: begin
            prdata_o[2:0] = prio_i[19][2:0];
            prio_re_o[19] = 1'b1;
          end
          32'hc000050: begin
            prdata_o[2:0] = prio_i[20][2:0];
            prio_re_o[20] = 1'b1;
          end
          32'hc000054: begin
            prdata_o[2:0] = prio_i[21][2:0];
            prio_re_o[21] = 1'b1;
          end
          32'hc000058: begin
            prdata_o[2:0] = prio_i[22][2:0];
            prio_re_o[22] = 1'b1;
          end
          32'hc00005c: begin
            prdata_o[2:0] = prio_i[23][2:0];
            prio_re_o[23] = 1'b1;
          end
          32'hc000060: begin
            prdata_o[2:0] = prio_i[24][2:0];
            prio_re_o[24] = 1'b1;
          end
          32'hc000064: begin
            prdata_o[2:0] = prio_i[25][2:0];
            prio_re_o[25] = 1'b1;
          end
          32'hc000068: begin
            prdata_o[2:0] = prio_i[26][2:0];
            prio_re_o[26] = 1'b1;
          end
          32'hc00006c: begin
            prdata_o[2:0] = prio_i[27][2:0];
            prio_re_o[27] = 1'b1;
          end
          32'hc000070: begin
            prdata_o[2:0] = prio_i[28][2:0];
            prio_re_o[28] = 1'b1;
          end
          32'hc000074: begin
            prdata_o[2:0] = prio_i[29][2:0];
            prio_re_o[29] = 1'b1;
          end
          32'hc000078: begin
            prdata_o[2:0] = prio_i[30][2:0];
            prio_re_o[30] = 1'b1;
          end
          32'hc001000: begin
            prdata_o[30:0] = ip_i[0][30:0];
            ip_re_o[0] = 1'b1;
          end
          32'hc002000: begin
            prdata_o[30:0] = ie_i[0][30:0];
            ie_re_o[0] = 1'b1;
          end
          32'hc002080: begin
            prdata_o[30:0] = ie_i[1][30:0];
            ie_re_o[1] = 1'b1;
          end
          32'hc200000: begin
            prdata_o[2:0] = threshold_i[0][2:0];
            threshold_re_o[0] = 1'b1;
          end
          32'hc201000: begin
            prdata_o[2:0] = threshold_i[1][2:0];
            threshold_re_o[1] = 1'b1;
          end
          32'hc200004: begin
            prdata_o[4:0] = cc_i[0][4:0];
            cc_re_o[0] = 1'b1;
          end
          32'hc201004: begin
            prdata_o[4:0] = cc_i[1][4:0];
            cc_re_o[1] = 1'b1;
          end
          default: pslverr_o = 1'b1;
        endcase
      end
    end
  end
endmodule

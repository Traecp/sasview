#if !defined(parallelepiped_h)
#define parallelepiped_h
#include "parameters.hh"

/** Structure definition for Parallelepiped parameters
 * [PYTHONCLASS] = ParallelepipedModel
 * [DISP_PARAMS] = short_a, short_b, long_c,parallel_phi,parallel_psi, parallel_theta
   [DESCRIPTION] = <text> Form factor for a rectangular solid with uniform scattering length density.

		scale:Scale factor
		short_a: length of short edge  [A]
		short_b: length of another short edge [A]
		long_c: length of long edge  of the parallelepiped [A]
		sldPipe: Pipe_sld
		sldSolv: solvent_sld
		background:Incoherent Background [1/cm]
		</text>
	[FIXED]= <text>short_a.width; short_b.width; long_c.width;parallel_phi.width;parallel_psi.width; parallel_theta.width</text>
	[ORIENTATION_PARAMS]= <text>parallel_phi;parallel_psi; parallel_theta; parallel_phi.width;parallel_psi.width; parallel_theta.width</text>


 **/

class ParallelepipedModel{
public:
  // Model parameters
  /// Scale factor
  //  [DEFAULT]=scale=1.0
  Parameter scale;
  ///  Length of short edge of the parallelepiped [A]
  //  [DEFAULT]=short_a=35 [A]
  Parameter short_a;
  /// Length of short edge edge of the parallelepiped [A]
  //  [DEFAULT]=short_b=75 [A]
  Parameter short_b;
  /// Length of long edge of the parallelepiped [A]
  //  [DEFAULT]=long_c=400 [A]
  Parameter long_c;
  /// SLD_Pipe [1/A^(2)]
  //  [DEFAULT]=sldPipe=6.3e-6 [1/A^(2)]
  Parameter sldPipe;
  /// sldSolv [1/A^(2)]
  //  [DEFAULT]=sldSolv=1.0e-6 [1/A^(2)]
  Parameter sldSolv;
  /// Incoherent Background [1/cm]
  //  [DEFAULT]=background=0.0 [1/cm]
  Parameter background;
  /// Orientation of the parallelepiped axis w/respect incoming beam [deg]
  //  [DEFAULT]=parallel_theta=0.0 [deg]
  Parameter parallel_theta;
  /// Orientation of the longitudinal axis of the parallelepiped in the plane of the detector [deg]
  //  [DEFAULT]=parallel_phi=0.0 [deg]
  Parameter parallel_phi;
  /// Orientation of the cross-sectional minor axis of the parallelepiped in the plane of the detector [deg]
  //  [DEFAULT]=parallel_psi=0.0 [deg]
  Parameter parallel_psi;

  // Constructor
  ParallelepipedModel();

  // Operators to get I(Q)
  double operator()(double q);
  double operator()(double qx, double qy);
  double calculate_ER();
  double calculate_VR();
  double evaluate_rphi(double q, double phi);
};
#endif

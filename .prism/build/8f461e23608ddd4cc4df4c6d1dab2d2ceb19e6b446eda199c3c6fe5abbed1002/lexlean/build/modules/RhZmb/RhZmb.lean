module
public import Init
public import LexLeanRuntime.Portable
public import RhZmb.Foundation.Library.V1.Model
set_option autoImplicit false
set_option maxRecDepth 100000
set_option maxHeartbeats 1000000000
set_option linter.constructorNameAsVariable false
namespace RhZmb.RhZmb

@[expose] public def identity (value : Nat) : Nat := value

@[expose] public def acceptance : Bool := (LexLeanRuntime.equal (identity (42)) (42) : Bool)

@[expose] public def rhzmbLibrary : RhZmb.Foundation.Library.V1.Model.NativeLibrary := ({ profile := "prismpm/native-library/1", name := "Riemann-Zero Multi-Brane", cargoName := "rh-zero-multi-brane", cargoVersion := "0.1.0", cargoDescription := "Formal F1-square multi-brane geometry and combinatorial bounds", cargoRepository := "https://github.com/UOR-Foundation/PrismPM", cargoHomepage := "https://github.com/UOR-Foundation/PrismPM", exportRoots := ("RhZmb.RhZmb.acceptance" :: ("RhZmb.RhZmb.identity" :: ([] : List (String)))), acceptanceRoots := ("RhZmb.RhZmb.acceptance" :: ([] : List (String))) } : RhZmb.Foundation.Library.V1.Model.NativeLibrary)

end RhZmb.RhZmb

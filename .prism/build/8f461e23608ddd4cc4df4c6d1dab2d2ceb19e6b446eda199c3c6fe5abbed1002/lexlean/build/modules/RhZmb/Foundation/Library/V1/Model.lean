module
public import Init
set_option autoImplicit false
set_option maxRecDepth 100000
set_option maxHeartbeats 1000000000
set_option linter.constructorNameAsVariable false
namespace RhZmb.Foundation.Library.V1.Model

public structure NativeLibrary where
  profile : String
  name : String
  cargoName : String
  cargoVersion : String
  cargoDescription : String
  cargoRepository : String
  cargoHomepage : String
  exportRoots : List (String)
  acceptanceRoots : List (String)

end RhZmb.Foundation.Library.V1.Model

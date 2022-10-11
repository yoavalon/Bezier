d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()

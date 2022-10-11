d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()

d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()

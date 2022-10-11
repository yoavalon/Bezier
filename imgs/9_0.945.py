d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()

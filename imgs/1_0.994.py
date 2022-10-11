d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()

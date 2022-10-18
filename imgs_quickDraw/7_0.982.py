d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)

d.end()

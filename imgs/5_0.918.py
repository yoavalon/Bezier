d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(3,0)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)

d.end()

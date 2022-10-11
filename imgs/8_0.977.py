d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()

d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)

d.end()

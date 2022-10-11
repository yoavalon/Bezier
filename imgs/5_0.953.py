d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)

d.end()
